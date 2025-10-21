import streamlit as st
from pages import skin, pneumonia, multidisease, heart  # Assuming a folder named pages

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="WBDPRS",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------- Background & Custom CSS ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to bottom right, #e0f7fa, #b2dfdb);
    font-family: 'Poppins', sans-serif;
    color: #004d40;
}
h1, h2, h3, p, label {
    color: #004d40;
}
section.main > div.block-container {
    padding-top: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
}
div.stButton > button {
    background-color: #26a69a;
    color: white;
    border-radius: 8px;
    height: 3em;
    width: 100%;
    font-size: 1.1rem;
    font-weight: bold;
}
div.stButton > button:hover {
    background-color: #00796b;
}
</style>
""", unsafe_allow_html=True)

# ---------------- App Header ----------------
st.markdown("<h1 style='text-align:center;'>Web-based Disease Prediction System</h1>", unsafe_allow_html=True)
st.write("---")

# ---------------- Tabs ----------------
tab_skin, tab_pneumonia, tab_multidisease, tab_heart = st.tabs(
    ["Skin Cancer", "Pneumonia", "Multidisease", "Heart Disease"]
)

with tab_skin:
    st.markdown("<h2 style='text-align:center;'>Skin Cancer Prediction</h2>", unsafe_allow_html=True)
    skin.skin()

with tab_pneumonia:
    st.markdown("<h2 style='text-align:center;'>Pneumonia Detection</h2>", unsafe_allow_html=True)
    pneumonia.pneumonia()

with tab_multidisease:
    st.markdown("<h2 style='text-align:center;'>Multidisease Prediction</h2>", unsafe_allow_html=True)
    multidisease.multidisease()

with tab_heart:
    st.markdown("<h2 style='text-align:center;'>Heart Disease Prediction</h2>", unsafe_allow_html=True)
    heart.heart()
