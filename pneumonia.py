import streamlit as st
import numpy as np
from keras.models import load_model
from tensorflow.keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from PIL import Image
from streamlit_option_menu import option_menu

def pneumonia():
    st.markdown("## Have a Quick Overlook :eyes:")
    st.text("Step I: Scroll down to check whether you have Pneumonia or not.")
    st.text("Step II: Choose either Camera input or Upload Image to provide an X-ray image.")
    st.text("Step III: Click Submit to see the prediction.\n")
    st.markdown("That's cool :sunglasses:")
    st.info("Note: This is an approximate model under development.")

    # Load model once
    model = load_model(r'model_vgg16.h5')

    # Option menu for input type
    selected_input = option_menu(
        None,
        ['Camera', 'Upload Image'],
        icons=['camera', 'image'],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "15px"},
            "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px",
                         "--hover-color": "#eee","--text-color":"#262730"},
            "nav-link-selected": {"background-color": "#6cdacf","--text-color":"#262730"},
        }
    )

    # Function to process and predict
    def predict_image(img):
        img = img.resize((224, 224)).convert('RGB')
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        classes = model.predict(x)

        # Handling prediction safely
        if classes.shape[1] == 2:
            pred_idx = np.argmax(classes[0])
            if pred_idx == 0:
                st.success("Normal")
            else:
                st.success("Pneumonia")
        else:
            st.warning("Unexpected model output shape.")

    # Camera input
    if selected_input == 'Camera':
        picture = st.camera_input("Take a picture")
        if picture is not None:
            img = Image.open(picture)
            st.image(img, width=500)
            predict_image(img)

    # Upload image
    elif selected_input == 'Upload Image':
        uploaded_file = st.file_uploader("Choose a file", type=['png','jpg','jpeg'])
        if uploaded_file is not None:
            img = Image.open(uploaded_file)
            st.image(img, width=500)
            predict_image(img)
