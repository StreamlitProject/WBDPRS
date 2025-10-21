import streamlit as st
import heart as h
import multidisease as m
import pneumonia as p
import skin as s

# -------------------- Page Configuration --------------------
st.set_page_config(
    page_title="WBDPRS",
    page_icon="🤖",
    layout="wide"
)

# -------------------- Custom CSS --------------------
st.markdown(
    """
    <style>
    .stApp {
        background: url("https://drive.google.com/uc?export=view&id=1QNZpRaGDbxsDO3ZyjURYTfIMePIMbQ4c");
        background-size: cover;
        background-attachment: fixed;
    }
    h1, h2 {
        text-align: center; 
        color: #0a9396;
        text-shadow: 1px 1px 2px #fff;
    }
    .nav-button {
        display: inline-block;
        margin: 0 8px;
        padding: 6px 16px;
        border-radius: 8px;
        background-color: #fafafa;
        color: #262730;
        font-weight: bold;
        cursor: pointer;
        transition: 0.3s;
    }
    .nav-button:hover {
        background-color: #6cdacf;
        color: #fff;
    }
    .nav-button-active {
        background-color: #0a9396;
        color: #fff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------- App Title --------------------
st.title("🤖 Web-based Disease Prediction System")

# -------------------- Horizontal Navigation Bar --------------------
if "page" not in st.session_state:
    st.session_state.page = "Skin Cancer"  # default page

# Define pages and optional icons
pages = {
    "Skin Cancer": {"func": s.skin, "icon": "🩺"},
    "Pneumonia": {"func": p.pneumonia, "icon": "🫁"},
    "Multidisease": {"func": m.multidisease, "icon": "💊"},
    "Heart Disease": {"func": h.heart, "icon": "❤️"},
}

# Render navigation buttons
cols = st.columns(len(pages))
for i, (name, info) in enumerate(pages.items()):
    if cols[i].button(f"{info['icon']} {name}"):
        st.session_state.page = name

st.markdown("<br>", unsafe_allow_html=True)  # spacing

# -------------------- Render Selected Page --------------------
current_page = st.session_state.page
st.markdown(f"<h2><u>{current_page}</u></h2>", unsafe_allow_html=True)
pages[current_page]["func"]()
