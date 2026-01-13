import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 1. 页面基本配置
st.set_page_config(page_title="CM Tennis Guide", layout="wide", page_icon="🎾")

# 2. 核心 CSS
st.markdown("""
    <style>
    .stApp, p, span, label { color: inherit !important; }
    h1, h2, h3 { color: #d4f01e !important; }
    .stButton>button {
        width: 100%;
        background-color: #2d5a27;
        color: white !important;
        border-radius: 20px;
        border: 1px solid #d4f01e;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 核心数据 (统一字段名称)
data = [
    {
        "name": "700th Anniversary Stadium / 700周年体育场",
        "lat": 18.8411, "lon": 98.9627,
        "price_en": "60-80 THB/hr", "price_cn": "60-80 铢/小时",
        "desc_en": "11 hard courts. Most affordable but busy in the evening.",
        "desc_cn": "全清迈性价比最高，11片场地。傍晚人很多。",
        "url": "https://maps.app.goo.gl/9uG5m6vFf2vYyvJ8A"
    },
    {
        "name": "Nawarat Tennis Club / Nawarat 俱乐部",
        "lat": 18.7845, "lon": 99.0042,
        "price_en": "50-100 THB", "price_cn": "50-100 铢",
        "desc_en": "Best social vibe. Join the 7 AM morning group.",
        "desc_cn": "社交氛围最好，推荐参加早上7点的早茶球局。",
        "url": "https://maps.app.goo.gl/w6XJpX6vF2vYyvJ8A"
    },
    {
        "name": "Nut Tennis Court / Nut 网球场",
        "lat": 18.8470, "lon": 98.9540,
        "price_en": "100-120 THB/hr", "price_cn": "100-120 铢/小时",
        "desc_en": "Quiet, scenic, and very well-maintained.",
        "desc_cn": "环境安静优雅，场地维护状态极佳。",
        "url": "https://maps.app.goo.gl/x7YKpX6vF2vYyvJ8A"
    },
    {
        "name": "Gymkhana Club / Gymkhana 体育会",
        "lat": 18.7770, "lon": 99.0060,
        "price_en": "150-300 THB", "price_cn": "150-300 铢",
        "desc_en": "Historic club with rare grass courts.",
        "desc_cn": "清迈最古老的俱乐部，有罕见的草地场。",
        "url": "https://maps.app.goo.gl/y8ZKpX6vF2vYyvJ8A"
    }
]

# --- 侧边栏 ---
lang = st.sidebar.radio("Language / 语言", ("English", "中文"))

# --- 主界面 ---
st.title("🎾 Chiang Mai Tennis 2026")

col_left, col_right = st.columns([1.5, 1])

with col_left:
    m = folium.Map(location=[18.8100, 98.9800], zoom_start=12)
    for point in data:
        folium.Marker(
            [point["lat"], point["lon"]],
            tooltip=point["name"],
            icon=folium.Icon(color="green", icon="info-sign")
        ).add_to(m)
    
    # 获取地图点击数据
    map_data = st_folium(m, height=450, width="100%")

with col_right:
    st.write("### 📝 Info / 信息")
    
    # 修复逻辑：检查点击的对象是否存在
    clicked_name = map_data.get("last_object_clicked_tooltip")
    
    if clicked_name:
        selected = next((item for item in data if item["name"] == clicked_name), None)
        if selected:
            st.success(f"**{selected['name']}**")
            # 根据语言显示对应的字段
            p_key = "price_en" if lang == "English" else "price_cn"
            d_key = "desc_en" if lang == "English" else "desc_cn"
            
            st.write(f"💰 **{selected[p_key]}**")
            st.write(selected[d_key])
            st.link_button("📍 Navigation / 导航", selected["url"])
    else:
        msg = "Click a marker on the map!" if lang == "English" else "请点击地图上的标记点！"
        st.info(msg)

st.divider()
st.caption("Data updated Jan 2026")
