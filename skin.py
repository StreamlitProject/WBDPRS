import streamlit as st
import numpy as np
from keras.models import load_model
from PIL import Image
from streamlit_option_menu import option_menu

def skin():
    st.markdown("## Have A Quick Overlook :eyes:")
    st.text("Step I: Scroll down to check what kind of skin lesion you have.")
    st.text("Step II: Choose either Camera input or Upload Image to provide a skin lesion image.")
    st.text("Step III: Click Submit to see the prediction.\n")
    st.markdown("That's cool :sunglasses:")
    st.info("Note: This is an approximate model under development")

    # Load the model
    model = load_model(r'best_model.h5')

    # Input selection
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

    # Class mapping
    classes = {
        0: 'Akiec : Actinic keratoses and intraepithelial carcinoma',
        1: 'Bcc : Basal cell carcinoma',
        2: 'Bkl : Benign lesions of the keratosis',
        3: 'Df : Dermatofibroma',
        4: 'Nv : Melanocytic nevi',
        5: 'Vasc : Vascular lesions',
        6: 'Mel : Melanoma'
    }

    def predict_image(img):
        img = img.resize((28,28)).convert('RGB')
        img_array = np.array(img).reshape(-1,28,28,3)
        result = model.predict(img_array)
        class_index = int(np.argmax(result[0]))
        st.success(classes[class_index])

    # Camera input
    if selected_input == 'Camera':
        picture = st.camera_input("Take a picture")
        if picture is not None:
            img = Image.open(picture)
            st.image(img, width=500)
            predict_image(img)

    # Upload input
    elif selected_input == 'Upload Image':
        uploaded_file = st.file_uploader("Choose a file", type=['png','jpg','jpeg'])
        if uploaded_file is not None:
            img = Image.open(uploaded_file)
            st.image(img, width=500)
            predict_image(img)
