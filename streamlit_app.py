import streamlit as st
import skin
import pneumonia
import multidisease
import heart

st.set_page_config(
    page_title="WBDPRS",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- Header ----------------
st.markdown(
    "<h1 style='text-align:center;color:#004d40;font-family:Roboto;'>Web-based Disease Prediction System 🤖</h1>",
    unsafe_allow_html=True
)
st.write("---")

# ---------------- Tabs ----------------
tab1, tab2, tab3, tab4 = st.tabs(
    ["Skin Cancer", "Pneumonia", "Multidisease", "Heart Disease"]
)

with tab1:
    skin.skin()

with tab2:
    pneumonia.pneumonia()

with tab3:
    multidisease.multidisease()

with tab4:
    heart.heart()
