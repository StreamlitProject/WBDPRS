import streamlit as st
import heart
import multidisease
import pneumonia
import skin

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="WBDPRS",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------- Custom CSS & Theme ----------------
st.markdown("""
<style>
/* App background gradient */
.stApp {
    background: linear-gradient(to bottom right, #e0f7fa, #80deea);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Headers & text */
h1, h2, h3, p, label {
    color: #004d40;
}

/* Tabs container padding */
section.main > div.block-container {
    padding-top: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
}

/* Buttons styling */
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
    color: white;
}

/* Info & warning boxes */
.css-1lcbmhc.e1fqkh3o3 {font-weight: bold; color: #004d40;}
</style>
""", unsafe_allow_html=True)

# ---------------- Header ----------------
st.markdown("<h1 style='text-align:center;'>Web-based Disease Prediction System</h1>", unsafe_allow_html=True)
st.write("---")

# ---------------- Tabs as Pages ----------------
tab_skin, tab_pneu, tab_multi, tab_heart = st.tabs(
    ["Skin Cancer", "Pneumonia", "Multidisease", "Heart Disease"]
)

with tab_skin:
    st.markdown("<h2 style='text-align:center;'>Skin Cancer Prediction</h2>", unsafe_allow_html=True)
    skin.skin()

with tab_pneu:
    st.markdown("<h2 style='text-align:center;'>Pneumonia Prediction</h2>", unsafe_allow_html=True)
    pneumonia.pneumonia()

with tab_multi:
    st.markdown("<h2 style='text-align:center;'>Multidisease Prediction</h2>", unsafe_allow_html=True)
    multidisease.multidisease()

with tab_heart:
    st.markdown("<h2 style='text-align:center;'>Heart Disease Prediction</h2>", unsafe_allow_html=True)
    heart.heart()
