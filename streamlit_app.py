import streamlit as st
import skin as s
import pneumonia as p
import multidisease as m
import heart as h

# -------------------- Page Config --------------------
st.set_page_config(
    page_title="WBDPRS",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------- Custom CSS & Theme --------------------
st.markdown("""
    <style>
    /* Background gradient */
    .stApp {
        font-family: 'Helvetica Neue', Arial, sans-serif;
        background: linear-gradient(to bottom right, #f0f4f8, #d9e2ec);
        color: #0f3d3e;
    }

    /* Headings */
    h1, h2, h3 {
        font-family: 'Helvetica Neue', sans-serif;
        color: #056676;
        text-align: center;
    }

    /* Buttons */
    div.stButton > button {
        background-color: #009688;
        color: white;
        border-radius: 8px;
        height: 3em;
        font-size: 1.1rem;
        font-weight: bold;
        width: 100%;
    }
    div.stButton > button:hover {
        background-color: #00796b;
        color: white;
    }

    /* Forms and container spacing */
    section.main > div.block-container {
        padding-top: 3rem;
        padding-left: 4rem;
        padding-right: 4rem;
    }

    /* Dark mode overrides */
    [data-theme="dark"] h1, [data-theme="dark"] h2, [data-theme="dark"] h3 {
        color: #80cbc4;
    }
    [data-theme="dark"] .stApp {
        background: linear-gradient(to bottom right, #102027, #263238);
        color: #e0f7fa;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------- Header --------------------
st.markdown("<h1>Web-based Disease Prediction System</h1>", unsafe_allow_html=True)
st.write("---")

# -------------------- Tabs as Pages --------------------
tab_skin, tab_pneu, tab_multi, tab_heart = st.tabs(
    ["Skin Cancer", "Pneumonia", "Multidisease", "Heart Disease"]
)

with tab_skin:
    st.markdown("<h2>Skin Cancer Prediction</h2>", unsafe_allow_html=True)
    s.skin()  # Call skin.py function

with tab_pneu:
    st.markdown("<h2>Pneumonia Prediction</h2>", unsafe_allow_html=True)
    p.pneumonia()  # Call pneumonia.py function

with tab_multi:
    st.markdown("<h2>Multidisease Prediction</h2>", unsafe_allow_html=True)
    m.multidisease()  # Call multidisease.py function

with tab_heart:
    st.markdown("<h2>Heart Disease Prediction</h2>", unsafe_allow_html=True)
    h.heart()  # Call heart.py function
