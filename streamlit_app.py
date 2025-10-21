import streamlit as st
import skin as s
import pneumonia as p
import multidisease as m
import heart as h

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="WBDPRS",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------- Global CSS ----------------
st.markdown("""
<style>
/* Font & Global Colors */
html, body, [class*="css"]  {
    font-family: 'Roboto', sans-serif;
}

/* Light theme */
[data-theme="light"] {
    --text-color: #004d40;
    --bg-color: #e0f7fa;
    --header-color: #00695c;
    --card-bg: #ffffff;
}

/* Dark theme */
[data-theme="dark"] {
    --text-color: #e0f7fa;
    --bg-color: #004d40;
    --header-color: #80cbc4;
    --card-bg: #1a374d;
}

/* App Background & Text */
.stApp {
    background: var(--bg-color);
    color: var(--text-color);
}

/* Headers */
h1, h2, h3 {
    color: var(--header-color);
    font-weight: 700;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
}

/* Buttons */
div.stButton > button {
    background-color: #26a69a;
    color: white;
    border-radius: 10px;
    height: 3em;
    font-weight: bold;
}
div.stButton > button:hover {
    background-color: #00796b;
}

/* Cards */
.stCard {
    background-color: var(--card-bg);
    border-radius: 10px;
    padding: 1rem;
    margin-bottom: 1rem;
    box-shadow: 0 3px 6px rgba(0,0,0,0.1);
}

/* Form padding */
section.main > div.block-container {
    padding-top: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Header ----------------
st.markdown("<h1 style='text-align:center;'>Web-based Disease Prediction System</h1>", unsafe_allow_html=True)
st.write("---")

# ---------------- Tabs as Pages ----------------
tab1, tab2, tab3, tab4 = st.tabs(["Skin Cancer", "Pneumonia", "Multidisease", "Heart Disease"])

with tab1:
    st.markdown("<h2 style='text-align:center;'>Skin Cancer Prediction</h2>", unsafe_allow_html=True)
    s.skin()

with tab2:
    st.markdown("<h2 style='text-align:center;'>Pneumonia Prediction</h2>", unsafe_allow_html=True)
    p.pneumonia()

with tab3:
    st.markdown("<h2 style='text-align:center;'>Multidisease Prediction</h2>", unsafe_allow_html=True)
    m.multidisease()

with tab4:
    st.markdown("<h2 style='text-align:center;'>Heart Disease Prediction</h2>", unsafe_allow_html=True)
    h.heart()
