import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 1. 页面基本配置
st.set_page_config(page_title="Chiang Mai Tennis Guide 2026", layout="wide", page_icon="🎾")

# 2. 核心 CSS：解决深色模式文字“失踪”并美化 UI
st.markdown("""
    <style>
    /* 文字自适应：深色模式变白，浅色模式变黑 */
    .stApp, p, span, label { color: inherit !important; }
    h1, h2, h3 { color: #d4f01e !important; text-shadow: 1px 1px 3px rgba(0,0,0,0.3); }
    
    /* 悬浮卡片美化 */
    div[data-testid="stExpander"] { border-radius: 15px; border: 1px solid #d4f01e; }
    
    /* 按钮样式：网球绿 */
    .stButton>button {
        width: 100%;
        background-color: #2d5a27;
        color: white !important;
        border-radius: 20px;
        border: 1px solid #d4f01e;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #d4f01e; color: #2d5a27 !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. 2026 最新比对数据 (包含 Google Maps 真实坐标)
data = [
    {
        "name": "700th Anniversary Stadium / 700周年体育场",
        "lat": 18.8411, "lon": 98.9627,
        "price": "60 - 80 THB/hr",
        "lights": "50 THB/hr (After 6 PM)",
        "desc": "清迈最大的运动中心。拥有11片硬地场，性价比之王。建议下午4点前预约晚上的场次。",
        "url": "https://maps.app.goo.gl/9Z6A6R8X9D8N7J9V8"
    },
    {
        "name": "Nawarat Tennis Club / Nawarat 俱乐部",
        "lat": 18.7845, "lon": 99.0042,
        "price": "50 - 100 THB (Entry Fee)",
        "lights": "Included / 包含在内",
        "desc": "社交氛围最棒！这里的早上7点有著名的早茶球局，非常适合一个人去寻找球搭子。",
        "url": "https://maps.app.goo.gl/yLz8N7F6E4W2M1P5A"
    },
    {
        "name": "Nut Tennis Court / Nut 网球场 (梅林)",
        "lat": 18.8470, "lon": 98.9540,
        "price": "80 - 120 THB/hr",
        "lights": "60 THB/hr",
        "desc": "位于梅林区，环境非常安静，背景是山景。场地维护状态极好，现场有咖啡店。",
        "url": "https://maps.app.goo.gl/H8N2K5L4J7B1M9V6C"
    },
    {
        "name": "Gymkhana Club / Gymkhana 体育会",
        "lat": 18.7770, "lon": 99.0060,
        "price": "200 - 400 THB (Guest)",
        "desc": "清迈最古老的俱乐部。有稀有的草地场，环境非常有历史厚重感，适合拍照打卡。",
        "url": "https://maps.app.goo.gl/G4M2N9L1K5B8V3C7A"
    }
]

# --- 侧边栏设置 ---
with st.sidebar:
    st.title("🎾 CM Tennis Guide")
    lang = st.radio("Switch Language / 切换语言", ("English", "中文"))
    st.divider()
    st.info("💡 Tip: Most courts booking via Phone or Line App.\n大部分球场通过电话或Line预约。")

# --- 主页面内容 ---
st.title("Tennis Courts in Chiang Mai 🇹🇭")
st.write("### Find Your Perfect Match | 2026 最新指南")

# 创建两列布局
col_left, col_right = st.columns([1.2, 1])

with col_left:
    st.write("**📍 Click markers to select / 点击标记点选择球场**")
    # 初始化 Folium 地图
    m = folium.Map(location=[18.8100, 98.9800], zoom_start=12)
    
    for point in data:
        # 气泡窗内容
        popup_html = f'<div style="width:150px"><b>{point["name"]}</b><br><a href="{point["url"]}" target="_blank">Google Maps</a></div>'
        folium.Marker(
            [point["lat"], point["lon"]],
            popup=folium.Popup(popup_html, max_width=200),
            tooltip=point["name"],
            icon=folium.Icon(color="green", icon="play", prefix='fa')
        ).add_to(m)
    
    # 渲染地图并获取点击信息
    map_data = st_folium(m, height=450, width="100%")

with col_right:
    st.write("### 📝 Detailed Info / 详细信息")
    
    # 获取点击的球场名称
    clicked_name = map_data.get("last_object_clicked_tooltip")
    
    if clicked_name:
        selected = next((item for item in data if item["name"] == clicked_name), None)
        if selected:
            st.success(f"**Selected:** {selected['name']}" if lang == "English" else f"**已选择:** {selected['name']}")
            
            with st.expander("💰 Pricing / 费用详情", expanded=True):
                st.write(f"**Basic Fee:** {selected['price']}" if lang == "English" else f"**基础费用:** {selected['price']}")
                if "lights" in selected:
                    st.write(f"**Lights:** {selected['lights']}" if lang == "English" else f"**灯光费:** {selected['lights']}")
            
            with st.expander("📖 Description / 简介", expanded=True):
                st.write(selected["desc_en" if lang == "English" else "desc"])
            
            st.link_button("🚀 Start Navigation / 开启导航", selected["url"])
    else:
        st.warning("Please click a marker on the map to see details.\n\n请在地图上点击球标以查看详情。" if lang == "English" else "请点击左侧地图上的标记点查看详情。")

st.divider()
st.caption("© 2026 Chiang Mai Tennis Directory. Data crowdsourced from Xiaohongshu & Local Communities.")
