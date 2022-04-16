import streamlit as st
from streamlit_option_menu import option_menu
from heart import *
from home import *
from multidisease import *
import heart as h
import multidisease as m


# basic page conifg static but changes in few parameters

st.set_page_config(
    page_title="WBDPRS",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title("Web-based Disease Prediction & Recommender System")
# NavBar standard for all
selected3 = option_menu(None, ['Home', 'Heart Disease', 'Skin Cancer', 'Catract', 'Pneumonia', 'Multidisease'],
                        icons=['house', 'heart', 'file-person', 'eye', 'clipboard-plus', 'file-medical'],
                        menu_icon="cast", default_index=0, orientation="horizontal",
                        styles={
                            "container": {"padding": "0!important", "background-color": "#fafafa"},
                            "icon": {"color": "black", "font-size": "15px"},
                            "nav-link": {"font-size": "15px", "text-align": "left", "margin": "0px",
                                         "--hover-color": "#eee"},
                            "nav-link-selected": {"background-color": "#6cdacf"},
                        }
                        )


def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''

    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url("https://drive.google.com/uc?export=view&id=13vhdzYq-NQyW-pzfJooTAfPsluAvsagA");
             https://drive.google.com/file/d/13vhdzYq-NQyW-pzfJooTAfPsluAvsagA/view?usp=sharing
             background-size: cover
         }}
         .css-12ttj6m{{background-color:rgba(217,25,33,255); }}
         body{{font-weight: bold;
               font-family:"Galaxy-BT", sans-serif}}
         .css-1cpxqw2{{font-weight:bold}}
         p, ol, ul, dl{{font-weight:bold;
                        text-align:center;
                        font-size:1.3rem;}}
	.viewerBadge_link__1S137 {{visibility:hidden;}}
	.css-ffhzg2 {{color:black;}}
	.css-16huue1{{color:black;}}
	.st-by {{color:black;}}
	.css-1595djx{{visibility:hidden;}}
	.menu-title[data-v-4323f8ce], .menu .nav-item[data-v-4323f8ce], .menu .nav-link[data-v-4323f8ce], hr[data-v-4323f8ce] {{color: #0c292f;}}

         </style>
         """,
        unsafe_allow_html=True
    )


set_bg_hack_url()

hide_st_style = """
		  <style>
		  #MainMenu {visibility: hidden;}
		  footer {visibility: hidden;}
		  .css-18e3th9{
		  padding: 1.5rem 0rem 0rem; 
		  }
		  .css-18e3th9 {
		  padding-left: 6rem;
          padding-right: 6rem;
		  }
		  h1{text-align: center;color:#6cdacf;text-shadow: 2px 0 0 #fff, -2px 0 0 #fff, 0 2px 0 #fff, 0 -2px 0 #fff, 1px 1px #fff, -1px -1px 0 #fff, 1px -1px 0 #fff, -1px 1px 0 #fff;}
		  </style>
		  """
st.markdown(hide_st_style, unsafe_allow_html=True)

if selected3 == "Home":
    home()
elif selected3 == "Heart Disease":
    st.write("Heart Disease")
    h.heart()
elif selected3 == "Multidisease":
    st.write("Multidisease")
    m.multidisease()
