import streamlit as st
import pandas as pd

# 1. 基础配置
st.set_page_config(
    page_title="Chiang Mai Tennis Guide 2026", 
    layout="wide", 
    page_icon="🎾"
)

# 2. 增强版 CSS (适配深色/浅色模式)
st.markdown("""
    <style>
    /* 确保在深色模式下，描述文字也能清晰可见 */
    .stMarkdown, p, span, label {
        color: inherit !important;
    }
    
    /* 强制标题在深色模式下呈现醒目的亮色，在浅色模式下呈现深绿色 */
    h1, h2, h3 {
        color: #d4f01e !important; /* 网球黄，深浅背景都清晰 */
    }

    /* 按钮样式优化 */
    .stButton>button {
        width: 100%;
        background-color: #2d5a27;
        color: white !important;
        border-radius: 20px;
        border: 2px solid #d4f01e;
    }
    
    /* 针对深色模式的容器微调 */
    [data-testid="stVerticalBlock"] > div > div {
        border-color: rgba(212, 240, 30, 0.3) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 核心数据 (包含导航链接)
data = [
    {
        "name_en": "700th Anniversary Stadium", 
        "name_cn": "700周年体育场", 
        "lat": 18.8402, "lon": 98.9644, 
        "url": "https://maps.app.goo.gl/Rx8sPD8MbubymMqB7",
        "price": "60 THB/hr", 
        "type": "Public",
        "desc_en": "The largest facility in town with 11 hard courts and practice walls. Great for finding partners in the evenings.",
        "desc_cn": "清迈最大的体育场，拥有11片硬地场和练习墙，是晚上找球友的最佳去处。"
    },
    {
        "name_en": "Nawarat Tennis Club", 
        "name_cn": "Nawarat 网球俱乐部", 
        "lat": 18.7845, "lon": 99.0042, 
        "url": "https://maps.app.goo.gl/3fR6pSzL5Z6VqY7v5",
        "price": "50 THB (Guest Fee)", 
        "type": "Club",
        "desc_en": "6 hard courts with a very active community. Famous for early morning pickup games (7:00 AM).",
        "desc_cn": "拥有6片硬地场，社群非常活跃。以早上7点的“早茶球局”而闻名。"
    },
    {
        "name_en": "Nut Tennis Court", 
        "name_cn": "Nut 网球场 (梅林)", 
        "lat": 18.8950, "lon": 98.9400, 
        "url": "https://maps.app.goo.gl/5eR7pSzL5Z6VqY7v5",
        "price": "80-100 THB/hr", 
        "type": "Private",
        "desc_en": "High-quality courts with a beautiful mountain backdrop in Mae Rim. Features a small cafe on site.",
        "desc_cn": "位于梅林区，球场质量极高，背景是优美的山景，现场还设有小型咖啡馆。"
    },
    {
        "name_en": "Gymkhana Club", 
        "name_cn": "Gymkhana 俱乐部", 
        "lat": 18.7770, "lon": 99.0060, 
        "url": "https://maps.app.goo.gl/1wR8pSzL5Z6VqY7v5",
        "price": "Member / Guest Pass", 
        "type": "Private",
        "desc_en": "The oldest sports club in the city. Offers a unique, traditional atmosphere with grass and hard court options.",
        "desc_cn": "清迈最古老的体育俱乐部，拥有独特的传统氛围，提供草地场和硬地场选择。"
    }
]
df = pd.DataFrame(data)

# --- 侧边栏 ---
with st.sidebar:
    st.title("🎾 Menu / 菜单")
    lang = st.radio("Select Language / 选择语言", ("English", "中文"))
    st.divider()
    st.caption("Updated: Jan 2026")

# --- 主界面：第一版简介内容 ---
if lang == "English":
    st.title("Tennis Courts in Chiang Mai")
    st.subheader("Your 2026 Guide to the Best Places to Play")
    st.write("---")
    st.write("### Find Your Perfect Match")
    st.write("Whether you're looking for professional clay, standard hard courts, or a friendly local pickup game, Chiang Mai offers some of the best tennis facilities in Northern Thailand.")
else:
    st.title("清迈网球场指南")
    st.subheader("2026 泰北玫瑰打球首选清单")
    st.write("---")
    st.write("### 寻找你的完美球场")
    st.write("无论你是想找专业的硬地场、还是轻松的本地业余球局，清迈作为泰北中心，拥有全泰国最棒的网球设施和氛围。")

# --- 地图 ---
st.map(df, color='#2d5a27')

st.write("---")

# --- 球场卡片详情 ---
cols = st.columns(2)

for i, court in enumerate(data):
    with cols[i % 2]:
        with st.container(border=True):
            if lang == "English":
                st.subheader(court["name_en"])
                st.write(f"📍 **Type:** {court['type']}")
                st.write(court["desc_en"])
                st.write(f"💰 **Price:** {court['price']}")
                st.link_button("📍 Open in Google Maps", court["url"])
            else:
                st.subheader(court["name_cn"])
                st.write(f"📍 **场地类型:** {court['type']}")
                st.write(court["desc_cn"])
                st.write(f"💰 **价格:** {court['price']}")
                st.link_button("📍 开启地图导航", court["url"])

# --- 页脚 ---
st.write("---")
if lang == "English":
    st.caption("© 2026 Chiang Mai Tennis Guide. Always call ahead to check court availability.")
else:
    st.caption("© 2026 清迈网球指南。建议在前往前先打电话确认场地可用性。")
