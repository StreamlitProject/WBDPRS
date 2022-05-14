import streamlit as st
from streamlit_option_menu import option_menu
from heart import *
from home import *
from multidisease import *
import heart as h
import multidisease as m
from pneumonia import *
import pneumonia as p
from skin import *
import skin as s


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

st.title("Web-based Disease Prediction System")
# NavBar standard for all
selected3 = option_menu(None, ['Home','Skin Cancer', 'Pneumonia', 'Multidisease'],
                        icons=['house','file-person', 'clipboard-plus', 'file-medical'],
                        menu_icon="cast", default_index=0, orientation="horizontal",
                        styles={
                            "container": {"padding": "0!important", "background-color": "#fafafa","color": "#262730"},
                            "icon": {"color": "black", "font-size": "15px"},
                            "nav-link": {"font-size": "15px", "text-align": "left", "margin": "0px",
                                         "--hover-color": "#6ddacf","--text-color":"#262730"},
                            "nav-link-selected": {"background-color": "#6cdacf","--text-color":"#262730"},
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
	 #root > div:nth-child(1) > div > div > div > div > section > div {{padding-top: 1rem;}}
	 /*setting background image*/
         .stApp {{
             background: url("https://drive.google.com/uc?export=view&id=1QNZpRaGDbxsDO3ZyjURYTfIMePIMbQ4c");
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
	
	.css-ffhzg2 {{color:black;}} /*form title color*/
	.css-16huue1{{color:black;}} /*text in form*/
	.st-by {{color:black;}}  /*text in form*/
	.css-1595djx{{visibility:hidden;}} /*upper tag hidden*/
	.st-dc{{background-color:white;}}  /*dropdown background*/
	.st-bu {{background-color:rgb(240,242,246);}}  /*dropdown flex color*/
	.st-bp {{color:black;}}  /*dropdown text*/
	.css-e3kofv {{background:rgb(240,242,246);}}  /*dropdown hover*/
	.css-1q8dd3e {{background:white;}}  /*clear button*/

	.css-1wgbv7k {{background-color:rgb(109,218,207);}} /*Camera Pneumnia*/
	.css-x8wxsk {{background-color:rgb(109,218,207);color:black;}} /*upload*/
	:root{{--text-color:black;}}
	.nav-item{{color:black;}}
	.nav-item[[data-v-4323f8ce]]{{color:black;}}
	.data-v-4323f8ce{{color:black;}}
	.css-eczf16{{display: none;}} /*hide the link on title*/
	.css-1xfuh55{{display: none;}} /*hide the link on images*/
	.css-6awftf{{display: none;}} /*hide the link on images*/
	
	/* this to remove all the things*/
	 div[data-testid="stToolbar"] {{
                visibility: hidden;
                height: 0%;
                position: fixed;
                }}
                div[data-testid="stDecoration"] {{
                visibility: hidden;
                height: 0%;
                position: fixed;
                }}
                div[data-testid="stStatusWidget"] {{
                visibility: hidden;
                height: 0%;
                position: fixed;
                }}
                #MainMenu {{
                visibility: hidden;
                height: 0%;
                }}
                header {{
                visibility: hidden;
                height: 0%;
                }}
                footer {{
                visibility: hidden;
                height: 0%;
                }}

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
elif selected3 == 'Pneumonia':
    st.write('Pneumonia')
    p.pneumonia()
elif selected3 == 'Skin Cancer':
    s.skin()


