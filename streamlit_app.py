import streamlit as st
from heart import heart
from multidisease import multidisease
from pneumonia import pneumonia
from skin import skin
from streamlit_extras.badges import badge
from streamlit_extras.let_it_rain import rain

st.set_page_config(
    page_title="WBDPRS Dashboard",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------- Custom CSS for dashboard ---------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #e0f7fa, #b2dfdb);
    font-family: 'Arial', sans-serif;
}
h1, h2, h3, p, label {
    color: #004d40;
}
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
section.main > div.block-container {
    padding-top: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
}
</style>
""", unsafe_allow_html=True)

# --------- Header ---------
st.markdown("<h1 style='text-align:center;'>🩺 Web-based Disease Prediction System</h1>", unsafe_allow_html=True)
st.write("---")

# --------- Sidebar Navigation ---------
option = st.sidebar.radio(
    "Select Disease Module",
    ["Skin Cancer", "Pneumonia", "Multidisease", "Heart Disease"],
    index=0
)

st.sidebar.markdown("#### About")
st.sidebar.info("Predict diseases based on symptoms or images. Supports Skin, Pneumonia, Heart, and Multidisease prediction.")

# Optional Rain animation for fun
rain(emoji="🩺", font_size=20, falling_speed=5, animation_length=3)

# --------- Main Content ---------
if option == "Skin Cancer":
    st.markdown("<h2 style='text-align:center;'>Skin Cancer Prediction</h2>", unsafe_allow_html=True)
    skin()
elif option == "Pneumonia":
    st.markdown("<h2 style='text-align:center;'>Pneumonia Prediction</h2>", unsafe_allow_html=True)
    pneumonia()
elif option == "Multidisease":
    st.markdown("<h2 style='text-align:center;'>Multidisease Prediction</h2>", unsafe_allow_html=True)
    multidisease()
elif option == "Heart Disease":
    st.markdown("<h2 style='text-align:center;'>Heart Disease Prediction</h2>", unsafe_allow_html=True)
    heart()
