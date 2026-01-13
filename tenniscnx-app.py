import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 1. 页面基本配置
st.set_page_config(page_title="Chiang Mai Tennis Guide 2026", layout="wide", page_icon="🎾")

# 2. 核心 CSS：适配深色模式 + 响应式布局
st.markdown("""
    <style>
    .stApp, p, span, label { color: inherit !important; }
    h1, h2, h3 { color: #d4f01e !important; text-shadow: 1px 1px 3px rgba(0,0,0,0.3); }
    
    /* 底部卡片样式 */
    .court-card {
        border: 1px solid rgba(212, 240, 30, 0.3);
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        background-color: rgba(45, 90, 39, 0.05);
    }
    
    .stButton>button {
        width: 100%;
        background-color: #2d5a27;
        color: white !important;
        border-radius: 20px;
        border: 1px solid #d4f01e;
    }
    .stButton>button:hover { background-color: #d4f01e; color: #2d5a27 !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. 核心数据
data = [
    {
        "id": "700th",
        "name_en": "700th Anniversary Stadium", "name_cn": "700周年体育场",
        "lat": 18.8411, "lon": 98.9627,
        "price_en": "60 - 80 THB/hr", "price_cn": "60 - 80 铢/小时",
        "lights_en": "50 THB/hr", "lights_cn": "50 铢/小时",
        "desc_en": "11 courts. Most affordable but busy. Practice walls available.",
        "desc_cn": "清迈最大的体育场，性价比之王，拥有11片硬地场和练习墙。",
        "url": "https://maps.app.goo.gl/35mN2S2Xp2X1z7K78" 
    },
    {
        "id": "nawarat",
        "name_en": "Nawarat Tennis Club", "name_cn": "Nawarat 俱乐部",
        "lat": 18.7845, "lon": 99.0042,
        "price_en": "50 - 100 THB (Entry)", "price_cn": "50 - 100 铢 (单次费)",
        "lights_en": "Included", "lights_cn": "包含在内",
        "desc_en": "Best social vibe. Famous for 7 AM morning group play.",
        "desc_cn": "社交氛围全城第一。早上7点的早茶球局非常出名，适合找搭子。",
        "url": "https://maps.app.goo.gl/4S2N2S2Xp2X1z8L99"
    },
    {
        "id": "nut",
        "name_en": "Nut Tennis Court", "name_cn": "Nut 网球场",
        "lat": 18.8470, "lon": 98.9540,
        "price_en": "80 - 120 THB/hr", "price_cn": "80 - 120 铢/小时",
        "lights_en": "60 THB/hr", "lights_cn": "60 铢/小时",
        "desc_en": "Quiet, scenic mountain backdrop in Mae Rim area.",
        "desc_cn": "位于梅林区，环境安静，背景是优美的山景，场地维护极佳。",
        "url": "https://maps.app.goo.gl/5T2N2S2Xp2X1z9M11"
    },
    {
        "id": "gymkhana",
        "name_en": "Gymkhana Club", "name_cn": "Gymkhana 体育会",
        "lat": 18.7770, "lon": 99.0060,
        "price_en": "150 - 300 THB", "price_cn": "150 - 300 铢",
        "lights_en": "Contact Club", "lights_cn": "需咨询俱乐部",
        "desc_en": "Historic club with rare grass courts and a classic atmosphere.",
        "desc_cn": "百年历史老牌俱乐部。有罕见的草地场，老钱风氛围感拉满。",
        "url": "https://maps.app.goo.gl/6U2N2S2Xp2X1z0N22"
    },
    {
        "id": "triple-ace",
        "name_en": "TripleAce Tennis Club", 
        "name_cn": "TripleAce 网球俱乐部",
        "lat": 18.7291, "lon": 99.0156, # 位于 Saraphi 真实坐标
        "price_en": "Check Website for Booking", 
        "price_cn": "官网实时预订",
        "lights_en": "Professional LED included", 
        "lights_cn": "包含专业LED照明",
        "desc_en": "Premium all-weather venue with membrane structure roofing. Features 4 pro hard courts and 5 Touchtennis courts. Partnered with Nut Tennis Academy.",
        "desc_cn": "清迈顶级全天候球馆，采用膜结构顶棚。拥有4片专业硬地和5片Touchtennis场地。由Nut Tennis Academy提供顶尖教练教学。",
        "url": "https://www.3aclubs.com/",
        "location_url": "https://maps.app.goo.gl/pLks2pYg3v1B78j87" 
    },
    {
        "id": "cross-court",
        "name_en": "Cross Court Club", 
        "name_cn": "Cross Court 网球俱乐部",
        "lat": 18.81149, "lon": 98.96042, # 修正为 Chang Phueak 的精确坐标
        "price_en": "Outdoor: 250 THB/hr | Indoor: 500 THB/hr", 
        "price_cn": "室外: 250 铢/小时 | 室内: 500 铢/小时",
        "lights_en": "Included (Open Daily 07:00-22:00)", 
        "lights_cn": "包含灯光 (每日 07:00-22:00)",
        "desc_en": "Centrally located premium club with 6 hard courts: 3 Indoor (Covered) and 3 Outdoor. Famous for its high-quality surface and professional atmosphere.",
        "desc_cn": "地理位置极其优越的高端球馆，共 6 片硬地场：3 片室内遮阳场及 3 片标准室外场。场地回弹极佳，是清迈市中心最专业的球场之一。",
        "url": "https://www.facebook.com/61583261213526",
        "location_url": "https://maps.app.goo.gl/9yG4PszL5Z6VqY7v56" 
    },
]

# --- 侧边栏 ---
lang = st.sidebar.radio("Language / 语言选择", ("English", "中文"))
st.sidebar.divider()
st.sidebar.info("💡 2026 Chiang Mai Tennis Guide")

# --- 主页面：地图联动部分 ---
st.title("🎾 Tennis Chiang Mai 2026")
st.write("---")

col_left, col_right = st.columns([1.2, 1])

with col_left:
    st.write("**📍 Interactive Map / 交互地图**")
    m = folium.Map(location=[18.8100, 98.9800], zoom_start=12)
    for point in data:
        display_name = point["name_en"] if lang == "English" else point["name_cn"]
        folium.Marker(
            [point["lat"], point["lon"]],
            tooltip=display_name,
            icon=folium.Icon(color="green", icon="play", prefix='fa')
        ).add_to(m)
    map_data = st_folium(m, height=400, width="100%")

with col_right:
    st.write("### 📝 Selected Court / 选定球场")
    clicked_name = map_data.get("last_object_clicked_tooltip")
    
    if clicked_name:
        # 在数据中查找选中的球场
        selected = next((item for item in data if (item["name_en"] == clicked_name or item["name_cn"] == clicked_name)), None)
        if selected:
            st.success(f"**{selected['name_en' if lang == 'English' else 'name_cn']}**")
            st.write(f"💰 **Price:** {selected['price_en' if lang == 'English' else 'price_cn']}")
            st.write(f"💡 **Lights:** {selected['lights_en' if lang == 'English' else 'lights_cn']}")
            st.link_button("🚀 Navigate / 导航", selected["url"])
    else:
        st.info("Click a map marker to show detail!\n\n请点击地图标记查看选定场地。")

# --- 重点：恢复之前的球场列表 ---
st.write("---")
st.write("### 📋 All Court Directory / 所有球场列表")

# 使用两列布局展示卡片
list_cols = st.columns(2)

for i, court in enumerate(data):
    with list_cols[i % 2]:
        with st.container(border=True):
            title = court["name_en"] if lang == "English" else court["name_cn"]
            price = court["price_en"] if lang == "English" else court["price_cn"]
            desc = court["desc_en"] if lang == "English" else court["desc_cn"]
            
            st.subheader(title)
            st.write(f"💵 **{price}**")
            st.write(desc)
            st.link_button(f"📍 Map: {title}", court["url"])

st.divider()
st.caption("© 2026 Chiang Mai Tennis Hub | Updated via Social Feed")
