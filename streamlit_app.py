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

# ---------------- Background & Font ----------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
    .stApp {
        font-family: 'Roboto', sans-serif;
    }
    .main-header {
        color: #004d40;
        text-align: center;
        font-size: 2.5rem;
        font-weight: 700;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------- Header ----------------
st.markdown("<div class='main-header'>Web-based Disease Prediction System 🤖</div>", unsafe_allow_html=True)
st.write("---")

# ---------------- Tabs as Pages ----------------
tab1, tab2, tab3, tab4 = st.tabs(
    ["Skin Cancer", "Pneumonia", "Multidisease", "Heart Disease"]
)

with tab1:
    st.header("Skin Cancer Prediction")
    skin.skin()

with tab2:
    st.header("Pneumonia Prediction")
    pneumonia.pneumonia()

with tab3:
    st.header("Multidisease Prediction")
    multidisease.multidisease()

with tab4:
    st.header("Heart Disease Prediction")
    heart.heart()
