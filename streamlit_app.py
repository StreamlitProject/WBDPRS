import streamlit as st
from streamlit_option_menu import option_menu

# Import pages
import heart as h
import multidisease as m
import pneumonia as p
import skin as s

# -------------------- Page Configuration --------------------
st.set_page_config(
    page_title="WBDPRS",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# Web-based Disease Prediction System"
    }
)

st.title("Web-based Disease Prediction System")

# -------------------- Navigation Bar --------------------
selected_page = option_menu(
    None,
    ['Skin Cancer', 'Pneumonia', 'Multidisease', 'Heart Disease', 'Home'],
    icons=['file-person', 'clipboard-plus', 'file-medical', 'heart', 'house'],
    menu_icon="cast",
    default_index=4,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa", "color": "#262730"},
        "icon": {"color": "black", "font-size": "15px"},
        "nav-link": {"font-size": "15px", "text-align": "left", "margin": "0px",
                     "--hover-color": "#6ddacf", "--text-color": "#262730"},
        "nav-link-selected": {"background-color": "#6cdacf", "--text-color": "#262730"},
    }
)

# -------------------- Background & Custom CSS --------------------
def set_background():
    st.markdown(
        """
        <style>
        .stApp {
            background: url("https://drive.google.com/uc?export=view&id=1QNZpRaGDbxsDO3ZyjURYTfIMePIMbQ4c");
            background-size: cover;
        }
        body, p, ol, ul, dl { font-weight:bold; text-align:center; font-size:1.3rem; }
        h1 { text-align:center; color:#6cdacf; 
             text-shadow: 2px 0 0 #fff, -2px 0 0 #fff, 0 2px 0 #fff, 0 -2px 0 #fff; }
        div[data-testid="stToolbar"], div[data-testid="stDecoration"], div[data-testid="stStatusWidget"], 
        #MainMenu, header, footer { visibility: hidden; height: 0%; }
        </style>
        """, unsafe_allow_html=True
    )

set_background()

# -------------------- Page Mapping --------------------
pages = {
    "Home": lambda: st.write("Welcome to the Web-based Disease Prediction System!"),
    "Heart Disease": h.heart,
    "Multidisease": m.multidisease,
    "Pneumonia": p.pneumonia,
    "Skin Cancer": s.skin
}

# -------------------- Render Selected Page --------------------
if selected_page in pages:
    st.markdown(f"<center><h2><strong><u>{selected_page}</u></strong></h2></center>", unsafe_allow_html=True)
    pages[selected_page]()
