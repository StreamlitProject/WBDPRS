import streamlit as st
from pages import heart, multidisease, pneumonia, skin  # Assume all are in a folder named pages

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="WBDPRS",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------- Global CSS for Modern UI ----------------
st.markdown("""
<style>
/* App background & font */
.stApp {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    background: linear-gradient(to bottom right, #87CEEB, #B0E0E6);
    color: #1B263B;
}

/* Headings */
h1, h2, h3 {
    font-family: 'Helvetica Neue', sans-serif;
    color: #0D1B2A;
    text-align: center;
    font-weight: 700;
}

/* Buttons */
div.stButton > button {
    background-color: #117A65;
    color: white;
    border-radius: 12px;
    height: 3em;
    font-size: 1.1rem;
    font-weight: bold;
    width: 100%;
}
div.stButton > button:hover {
    background-color: #0E6655;
}

/* Container cards */
section.main > div.block-container {
    padding: 2rem 3rem;
    background-color: rgba(255, 255, 255, 0.85);
    border-radius: 16px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}

/* Alerts and widgets keep default colors for contrast */
</style>
""", unsafe_allow_html=True)

# ---------------- Header ----------------
st.markdown("<h1>Web-based Disease Prediction System</h1>", unsafe_allow_html=True)
st.write("---")

# ---------------- Sidebar Navigation ----------------
st.sidebar.header("Select Prediction Type")
page = st.sidebar.radio(
    "Navigate",
    ["Skin Cancer", "Pneumonia", "Multidisease", "Heart Disease"],
    index=0,
    horizontal=False
)

# ---------------- Render Selected Page ----------------
if page == "Skin Cancer":
    st.markdown("<h2>Skin Cancer Prediction</h2>", unsafe_allow_html=True)
    skin.skin()
elif page == "Pneumonia":
    st.markdown("<h2>Pneumonia Prediction</h2>", unsafe_allow_html=True)
    pneumonia.pneumonia()
elif page == "Multidisease":
    st.markdown("<h2>Multidisease Prediction</h2>", unsafe_allow_html=True)
    multidisease.multidisease()
elif page == "Heart Disease":
    st.markdown("<h2>Heart Disease Prediction</h2>", unsafe_allow_html=True)
    heart.heart()
