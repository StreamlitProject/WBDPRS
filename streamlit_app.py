import streamlit as st
import heart as h
import multidisease as m
import pneumonia as p
import skin as s

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="WBDPRS",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------- Background & Theme ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to bottom right, #e0f7fa, #e0f2f1);
    color: #004d40;
    font-family: 'Arial', sans-serif;
}
h1, h2, h3, p, label {
    color: #004d40;
}
section.main > div.block-container {
    padding-top: 3rem;
    padding-left: 4rem;
    padding-right: 4rem;
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
    color: white;
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
