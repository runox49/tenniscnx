import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 1. 页面配置
st.set_page_config(page_title="CM Tennis Guide", layout="wide")

# 2. CSS 修复深色模式文字消失
st.markdown("""
    <style>
    .stApp, p, span { color: inherit !important; }
    h1, h2, h3 { color: #d4f01e !important; }
    .stButton>button { background-color: #2d5a27; color: white !important; border-radius: 15px; }
    /* 让地图容器有圆角 */
    .folium-map { border-radius: 12px; }
    </style>
    """, unsafe_allow_html=True)

# 3. 核心数据 (含真实经纬度与信息)
data = [
    {
        "name": "700th Anniversary Stadium / 700周年体育场",
        "lat": 18.8396, "lon": 98.9594,
        "price": "60-80 THB/hr",
        "desc": "清迈最大的公立场地，拥有11片硬地场。傍晚非常热闹。",
        "url": "https://www.google.com/maps/search/?api=1&query=700th+Anniversary+of+Chiang+Mai+Stadium"
    },
    {
        "name": "Nawarat Tennis Club / Nawarat 俱乐部",
        "lat": 18.7958, "lon": 98.9962,
        "price": "50-100 THB (Guest)",
        "desc": "社交氛围全城最好，适合单人前往加入早晨7点的球局。",
        "url": "https://www.google.com/maps/search/?api=1&query=Nawarath+Tennis+Club"
    },
    {
        "name": "Nut Tennis Court / Nut 网球场",
        "lat": 18.8475, "lon": 98.9541,
        "price": "100-120 THB/hr",
        "desc": "梅林区高品质私人球场，环境安静且维护极好。",
        "url": "https://www.google.com/maps/search/?api=1&query=Nut+Tennis+Court"
    },
    {
        "name": "Gymkhana Club / Gymkhana 俱乐部",
        "lat": 18.7749, "lon": 99.0090,
        "price": "150-300 THB (Guest)",
        "desc": "百年历史俱乐部，提供清迈罕见的草地场体验。",
        "url": "https://www.google.com/maps/search/?api=1&query=Chiang+Mai+Gymkhana+Club"
    }
]

# --- 界面展示 ---
st.title("🎾 清迈网球指南 2026")

# 创建两列布局：左侧是小地图，右侧是简介
col_map, col_info = st.columns([1, 1])

with col_map:
    st.write("### 📍 交互地图")
    # 创建 Folium 地图对象
    m = folium.Map(location=[18.8100, 98.9800], zoom_start=12, tiles="OpenStreetMap")
    
    # 添加点击可交互的 POI
    for point in data:
        popup_content = f"""
        <div style="font-family: sans-serif; min-width: 150px;">
            <h4 style="margin:0; color:#2d5a27;">{point['name']}</h4>
            <p style="margin:5px 0; font-size:12px;">{point['desc']}</p>
            <a href="{point['url']}" target="_blank" style="color:#d4f01e; font-weight:bold;">开启导航</a>
        </div>
        """
        folium.Marker(
            [point["lat"], point["lon"]],
            popup=popup_content,
            tooltip=point["name"],
            icon=folium.Icon(color="green", icon="info-sign")
        ).add_to(m)
    
    # 在 Streamlit 中渲染地图（限制高度使其“变小”）
    map_data = st_folium(m, height=400, width=None)

with col_info:
    st.write("### 📝 选定球场简要信息")
    # 逻辑：如果用户点击了地图上的 POI，在右侧显示详细信息
    if map_data and map_data.get("last_object_clicked_tooltip"):
        clicked_name = map_data["last_object_clicked_tooltip"]
        # 寻找对应的数据
        selected_court = next((item for item in data if item["name"] == clicked_name), None)
        
        if selected_court:
            st.success(f"已选中: {selected_court['name']}")
            st.write(f"💰 **价格:** {selected_court['price']}")
            st.write(f"📖 **简介:** {selected_court['desc']}")
            st.link_button("🚀 立即导航前往", selected_court["url"])
    else:
        st.info("请在左侧地图上点击球场图标，查看详细费用与说明。")

st.divider()

# --- 底部列表（备选） ---
st.write("### 📋 快速概览")
st.dataframe(pd.DataFrame(data)[["name", "price"]], use_container_width=True)
