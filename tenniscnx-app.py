import streamlit as st
import pandas as pd

# 1. 基础配置
st.set_page_config(
    page_title="Chiang Mai Tennis Guide 2026", 
    layout="wide", 
    page_icon="🎾"
)

# 2. 注入自定义 CSS 样式 (替代 config.toml)
st.markdown("""
    <style>
    /* 调整主背景颜色 */
    .stApp {
        background-color: #f8f9f6;
    }
    /* 调整卡片和按钮的品牌色 */
    .stButton>button {
        background-color: #2d5a27;
        color: white;
        border-radius: 8px;
    }
    .stButton>button:hover {
        border-color: #d4f01e;
        color: #d4f01e;
    }
    /* 调整标题颜色 */
    h1, h2, h3 {
        color: #2d5a27 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 数据准备 ---
data = [
    {"name_en": "700th Anniversary Stadium", "name_cn": "700周年体育场", "lat": 18.8402, "lon": 98.9644, "price": "60 THB/hr", "type": "Public", "vibe_en": "Professional", "vibe_cn": "专业"},
    {"name_en": "Nawarat Tennis Club", "name_cn": "Nawarat 网球俱乐部", "lat": 18.7845, "lon": 99.0042, "price": "50 THB (Guest)", "type": "Club", "vibe_en": "Social", "vibe_cn": "社交"},
    {"name_en": "Nut Tennis Court", "name_cn": "Nut 网球场 (梅林)", "lat": 18.8950, "lon": 98.9400, "price": "80-100 THB/hr", "type": "Private", "vibe_en": "Scenic", "vibe_cn": "优美"},
    {"name_en": "Gymkhana Club", "name_cn": "Gymkhana 俱乐部", "lat": 18.7770, "lon": 99.0060, "price": "Member / Pass", "type": "Private", "vibe_en": "Historic", "vibe_cn": "历史感"}
]
df = pd.DataFrame(data)

# --- 侧边栏 ---
with st.sidebar:
    st.title("🎾 Menu / 菜单")
    lang = st.radio("Language / 语言", ("English", "中文"))
    st.divider()
    st.info("💡 **Tip:** Most courts require booking 1 day in advance.\n\n大部分球场建议提前一天预定。" if lang == "English" else "💡 **建议：** 大部分球场需提前1天预约。")

# --- 主界面 ---
if lang == "English":
    st.title("Chiang Mai Tennis Guide 2026")
    st.write("Find the best place to hit the ball in the Rose of the North.")
else:
    st.title("2026 清迈网球指南")
    st.write("带你发现泰北玫瑰最适合挥拍的场地。")

# --- 地图 ---
st.map(df, color='#2d5a27')

# --- 详情列表 ---
st.divider()
cols = st.columns(2)

for i, court in enumerate(data):
    with cols[i % 2]:
        with st.container(border=True):
            if lang == "English":
                st.subheader(court["name_en"])
                st.write(f"🏷️ **Type:** {court['type']} | 💰 **Price:** {court['price']}")
                st.write(f"✨ **Vibe:** {court['vibe_en']}")
                if st.button(f"View details for {court['name_en']}", key=f"en_{i}"):
                    st.balloons()
            else:
                st.subheader(court["name_cn"])
                st.write(f"🏷️ **类型:** {court['type']} | 💰 **价格:** {court['price']}")
                st.write(f"✨ **氛围:** {court['vibe_cn']}")
                if st.button(f"查看 {court['name_cn']} 详情", key=f"cn_{i}"):
                    st.balloons()

# --- 页脚 ---
st.markdown("---")
st.caption("Updated Jan 2026 | Built with ❤️ and Streamlit")
