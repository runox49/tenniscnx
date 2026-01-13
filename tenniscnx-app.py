import streamlit as st
import pandas as pd

# 1. 基础配置
st.set_page_config(
    page_title="CM Tennis Map 2026", 
    layout="wide", 
    page_icon="🎾"
)

# 2. 注入网球主题 CSS
st.markdown("""
    <style>
    .stApp { background-color: #fcfdf9; }
    .stButton>button {
        width: 100%;
        background-color: #2d5a27;
        color: white;
        border-radius: 20px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #d4f01e;
        color: #2d5a27;
        border: 1px solid #2d5a27;
    }
    h3 { color: #2d5a27 !important; margin-bottom: 0.5rem; }
    .css-1r6slb0 { border-radius: 12px; }
    </style>
    """, unsafe_allow_html=True)

# 3. 核心数据 (已更新 Google Maps 真实坐标及导航链接)
data = [
    {
        "name_en": "700th Anniversary Stadium", 
        "name_cn": "700周年体育场", 
        "lat": 18.8402, "lon": 98.9644, 
        "url": "https://maps.app.goo.gl/3XpXGZpS6v2A2uWz5",
        "price": "60 THB/hr", 
        "type": "Public",
        "vibe_cn": "专业、场地多",
        "vibe_en": "Pro & Many Courts"
    },
    {
        "name_en": "Nawarat Tennis Club", 
        "name_cn": "Nawarat 网球俱乐部", 
        "lat": 18.7845, "lon": 99.0042, 
        "url": "https://maps.app.goo.gl/vA8T6v2uE7Q8qL9s7",
        "price": "50-100 THB", 
        "type": "Club",
        "vibe_cn": "社交氛围浓厚",
        "vibe_en": "Social & Friendly"
    },
    {
        "name_en": "Nut Tennis Court", 
        "name_cn": "Nut 网球场 (Mae Rim)", 
        "lat": 18.8950, "lon": 98.9400, 
        "url": "https://maps.app.goo.gl/YfSgWnB6XvXw5pE9A",
        "price": "80-120 THB/hr", 
        "type": "Private",
        "vibe_cn": "环境优美、维护好",
        "vibe_en": "Boutique & Scenic"
    },
    {
        "name_en": "Gymkhana Club", 
        "name_cn": "Gymkhana 俱乐部", 
        "lat": 18.7770, "lon": 99.0060, 
        "url": "https://maps.app.goo.gl/B9U8P7v4T8xW3mK89",
        "price": "Member/Guest", 
        "type": "Private",
        "vibe_cn": "百年老店、有草地",
        "vibe_en": "Historic & Classic"
    }
]
df = pd.DataFrame(data)

# --- 侧边栏 ---
with st.sidebar:
    st.title("🎾 CM Tennis Map")
    lang = st.radio("Switch Language / 切换语言", ("English", "中文"))
    st.divider()
    if lang == "English":
        st.info("Click the buttons below the cards to start Google Maps navigation.")
    else:
        st.info("点击下方卡片中的按钮即可开启 Google 地图导航。")

# --- 主界面 ---
if lang == "English":
    st.title("Chiang Mai Tennis Guide 2026")
    st.subheader("Tap markers to see locations")
else:
    st.title("2026 清迈网球地图指南")
    st.subheader("点击地图标记查看位置")

# 地图展示 (使用网球绿配色)
st.map(df, color='#2d5a27', size=20)

st.divider()

# --- 球场卡片 ---
cols = st.columns(2)

for i, court in enumerate(data):
    with cols[i % 2]:
        with st.container(border=True):
            if lang == "English":
                st.subheader(court["name_en"])
                st.write(f"💰 **Price:** {court['price']}")
                st.write(f"🌟 **Vibe:** {court['vibe_en']}")
                st.link_button("📍 Open in Google Maps", court["url"])
            else:
                st.subheader(court["name_cn"])
                st.write(f"💰 **价格:** {court['price']}")
                st.write(f"🌟 **氛围:** {court['vibe_cn']}")
                st.link_button("📍 开启地图导航", court["url"])

# --- 页脚 ---
st.markdown("---")
st.caption("2026 Chiang Mai Tennis Hub | Data for reference only.")
