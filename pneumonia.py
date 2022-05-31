import streamlit as st
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from PIL import Image
#from io import BytesIO
#import urllib

#besturl='https://drive.google.com/file/d/1giYPPAkdfWIjXXrBJVDoB8EWkbcXh5-r/view?usp=sharing'
#besturl='https://drive.google.com/uc?id=' + besturl.split('/')[-2]


def pneumonia():
    with st.expander("Key Facts"):
        st.write("""
        1. Pneumonia accounts for 14% of all deaths of children under 5 years old, killing 740 180 children in 2019 \n
        2. Pneumonia can be caused by viruses, bacteria, or fungi. \n
        3. Pneumonia can be prevented by immunization, adequate nutrition, and by addressing environmental factors.\n
        4. Pneumonia caused by bacteria can be treated with antibiotics, but only one third of children with pneumonia receive the antibiotics they need.
     """)
    with st.expander("Causes"):
        st.write("""
        Pneumonia is caused by a number of infectious agents, including viruses, bacteria and fungi. The most common are:

        1. Streptococcus pneumoniae – the most common cause of bacterial pneumonia in children \n
        2. Haemophilus influenzae type b (Hib) – the second most common cause of bacterial pneumonia \n
        3. Respiratory syncytial virus is the most common viral cause of pneumonia \n
        4. In infants infected with HIV, Pneumocystis jiroveci is one of the most common causes of pneumonia, responsible for at least one quarter of all pneumonia deaths in HIV-infected infants.
     """)
    with st.expander("Transmission"):
        st.write("""
        Pneumonia can be spread in a number of ways.
        The viruses and bacteria that are commonly found in a child's nose or throat, can infect the lungs if they are inhaled. 
        They may also spread via air-borne droplets from a cough or sneeze. 
        In addition, pneumonia may spread through blood, especially during and shortly after birth. 
        More research needs to be done on the different pathogens causing pneumonia and the ways they are transmitted, as this is of critical importance for treatment and prevention.
     """)
     with st.expander("Risk Factors"):
            st.write("""
        The following environmental factors also increase a child's susceptibility to pneumonia:

        1. indoor air pollution caused by cooking and heating with biomass fuels (such as wood or dung)
        2. living in crowded homes
        3. parental smoking.
        """)
      with st.expander("Treatment"):
        st.write("""
        Pneumonia should be treated with antibiotics. 
        The antibiotic of choice for first line treatment is amoxicillin dispersible tablets. 
        Most cases of pneumonia require oral antibiotics, which are often prescribed at a health centre. 
        These cases can also be diagnosed and treated with inexpensive oral antibiotics at the community level by trained community health workers. 
        Hospitalization is recommended only for severe cases of pneumonia.
        """)
      with st.expander("Prevention"):
        st.write("""
        Preventing pneumonia in children is an essential component of a strategy to reduce child mortality. Immunization against Hib, pneumococcus, measles and whooping cough (pertussis) is the most effective way to prevent pneumonia.
        Adequate nutrition is key to improving children's natural defences, starting with exclusive breastfeeding for the first 6 months of life. In addition to being effective in preventing pneumonia, it also helps to reduce the length of the illness if a child does become ill.
        Addressing environmental factors such as indoor air pollution (by providing affordable clean indoor stoves, for example) and encouraging good hygiene in crowded homes also reduces the number of children who fall ill with pneumonia.
        In children infected with HIV, the antibiotic cotrimoxazole is given daily to decrease the risk of contracting pneumonia.
        """)
    
    model = load_model(r'model_vgg16.h5')
    selected1 = option_menu(None, ['Camera','Upload Image'],
                            icons=['camera','image'], 
                            menu_icon="cast", default_index=0, orientation="horizontal",
                            styles={"container": {"padding": "0!important", "background-color": "#fafafa"},"icon": {"color": "black", "font-size": "15px"}, "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee","--text-color":"#262730"},"nav-link-selected": {"background-color": "#6cdacf","--text-color":"#262730"},})

    if selected1=='Camera':
        picture = st.camera_input("Take a picture")
        if picture is not None:
            an_image = Image.open(picture)
            st.image(an_image,width=500)
            an_image = an_image.resize((224,224))
            an_image = an_image.convert('RGB')
            #st.write(type(an_image))
            x = image.img_to_array(an_image)
            #st.write(x)
            #st.write(x.dtype)
            #st.write(x.shape)
            x = np.expand_dims(x,axis=0)
            img_data = preprocess_input(x)
            classes = model.predict(x)
            if int(classes[0][0])==1:
                st.success("Normal")
            elif int(classes[0][1])==1:
                st.success("Pneumonia")
    elif selected1=='Upload Image':
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
            an_image = Image.open(uploaded_file)
            st.image(an_image,width=500)
            an_image = an_image.resize((224,224))
            an_image = an_image.convert('RGB')
            #st.write(type(an_image))
            x = image.img_to_array(an_image)
            #st.write(x)
            #st.write(x.dtype)
            #st.write(x.shape)
            x = np.expand_dims(x,axis=0)
            img_data = preprocess_input(x)
            classes = model.predict(x)
            if int(classes[0][0])==1:
                st.success("Normal")
            elif int(classes[0][1])==1:
                st.success("Pneumonia")

