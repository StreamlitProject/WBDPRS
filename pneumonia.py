import streamlit as st
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu
from keras.models import load_model
from tensorflow.keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from PIL import Image
#from io import BytesIO
#import urllib

#besturl='https://drive.google.com/file/d/1giYPPAkdfWIjXXrBJVDoB8EWkbcXh5-r/view?usp=sharing'
#besturl='https://drive.google.com/uc?id=' + besturl.split('/')[-2]


def pneumonia():
    with st.container():
        st.markdown("Have A Quick Overlook :eyes:")
        st.text("Step I: Go down in this webpage, where you find a template to check whether you have Pneumonia or Not")
        st.text("Step II: Here we have 2 options to choose 1.upload image 2. camera input, with  the help of this take X-ray image")
        st.text("Step III: Now click on submit.\n")
        st.markdown("That's cool :sunglasses:")
        st.info("Note: This is a approximate model, under development")
        st.text("\n\n\n")
    
    st.write("\n\n\n")
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

