import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 1. 页面基本配置
st.set_page_config(page_title="Chiang Mai Tennis Guide 2026", layout="wide", page_icon="🎾")

# 2. 核心 CSS：适配深色模式 + 品牌绿
st.markdown("""
    <style>
    .stApp, p, span, label { color: inherit !important; }
    h1, h2, h3 { color: #d4f01e !important; text-shadow: 1px 1px 3px rgba(0,0,0,0.3); }
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

# 3. 核心数据 (统一字段，确保不报错)
data = [
    {
        "name": "700th Anniversary Stadium / 700周年体育场",
        "lat": 18.8411, "lon": 98.9627,
        "price_en": "60 - 80 THB/hr",
        "price_cn": "60 - 80 铢/小时",
        "lights_en": "50 THB/hr (After 6 PM)",
        "lights_cn": "50 铢/小时 (晚6点后)",
        "desc_en": "11 courts. Most affordable but busy. Practice walls available.",
        "desc_cn": "清迈最大的体育场，性价比之王，拥有11片硬地场和练习墙。",
        "url": "https://maps.app.goo.gl/9QZzVz9ZzVz9ZzVz9" 
    },
    {
        "name": "Nawarat Tennis Club / Nawarat 俱乐部",
        "lat": 18.7845, "lon": 99.0042,
        "price_en": "50 - 100 THB (Entry Fee)",
        "price_cn": "50 - 100 铢 (单次入场费)",
        "lights_en": "Included",
        "lights_cn": "包含在内",
        "desc_en": "Best social vibe. Famous for 7 AM morning group play.",
        "desc_cn": "社交氛围全城第一。早上7点的早茶球局非常出名，适合找搭子。",
        "url": "https://maps.app.goo.gl/9QZzVz9ZzVz9ZzVz8"
    },
    {
        "name": "Nut Tennis Court / Nut 网球场",
        "lat": 18.8470, "lon": 98.9540,
        "price_en": "80 - 120 THB/hr",
        "price_cn": "80 - 120 铢/小时",
        "lights_en": "60 THB/hr",
        "lights_cn": "60 铢/小时",
        "desc_en": "Quiet, scenic mountain backdrop in Mae Rim area.",
        "desc_cn": "位于梅林区，环境安静，背景是优美的山景，场地维护极佳。",
        "url": "https://maps.app.goo.gl/9QZzVz9ZzVz9ZzVz7"
    },
    {
        "name": "Gymkhana Club / Gymkhana 体育会",
        "lat": 18.7770, "lon": 99.0060,
        "price_en": "150 - 300 THB (Guest rate)",
        "price_cn": "150 - 300 铢 (访客价)",
        "lights_en": "Check with club",
        "lights_cn": "需咨询俱乐部",
        "desc_en": "Historic club with rare grass courts and a classic atmosphere.",
        "desc_cn": "百年历史老牌俱乐部。有罕见的草地场，老钱风氛围感拉满。",
        "url": "https://maps.app.goo.gl/9QZzVz9ZzVz9ZzVz6"
    }
]

# --- 逻辑控制 ---
lang = st.sidebar.radio("Language / 语言", ("English", "中文"))

# --- 主页面 ---
st.title("Tennis Chiang Mai 2026")
st.write("---")

col_left, col_right = st.columns([1.2, 1])

with col_left:
    st.write("**📍 Click markers to see details / 点击标记点查看详情**")
    # 创建地图
    m = folium.Map(location=[18.8100, 98.9800], zoom_start=12)
    for point in data:
        folium.Marker(
            [point["lat"], point["lon"]],
            tooltip=point["name"],
            icon=folium.Icon(color="green", icon="play", prefix='fa')
        ).add_to(m)
    
    # 获取地图数据
    map_data = st_folium(m, height=450, width="100%")

with col_right:
    st.write("### 📝 Detailed Information")
    
    # 联动显示逻辑
    clicked_name = map_data.get("last_object_clicked_tooltip")
    
    if clicked_name:
        selected = next((item for item in data if item["name"] == clicked_name), None)
        if selected:
            st.success(f"**{selected['name']}**")
            
            # 动态选择语言键值
            p_key = "price_en" if lang == "English" else "price_cn"
            l_key = "lights_en" if lang == "English" else "lights_cn"
            d_key = "desc_en" if lang == "English" else "desc_cn"
            
            with st.container(border=True):
                st.write(f"💰 **Price:** {selected[p_key]}" if lang == "English" else f"💰 **基础价格:** {selected[p_key]}")
                st.write(f"💡 **Lights:** {selected[l_key]}" if lang == "English" else f"💡 **灯光费:** {selected[l_key]}")
                st.write("---")
                st.write(selected[d_key])
                st.link_button("🚀 Start Navigation / 导航", selected["url"])
    else:
        st.info("Please click a marker on the map!\n\n请在地图上点击球标查看详情。" if lang == "English" else "请在左侧地图上点击标记点！")

st.divider()
st.caption("© 2026 Chiang Mai Tennis Guide | Crowd-sourced via Xiaohongshu")
