import streamlit as st
import numpy as np
from keras.models import load_model
from PIL import Image

def skin():
    st.markdown("## Have a Quick Overlook :eyes:")
    st.text("Step I: Scroll down to check what kind of skin lesion you have.")
    st.text("Step II: Choose either Camera input or Upload Image to provide a skin lesion image.")
    st.text("Step III: Click Submit to see the prediction.\n")
    st.markdown("That's cool :sunglasses:")
    st.info("Note: This is an approximate model under development")

    model = load_model('best_model.h5')

    selected_input = st.radio("Select Input Method", ['Camera', 'Upload Image'], horizontal=True)

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
        st.success(f"Predicted Class: {classes[class_index]}")

    if selected_input == 'Camera':
        picture = st.camera_input("Take a picture")
        if picture:
            img = Image.open(picture)
            st.image(img, width=500)
            predict_image(img)

    else:
        uploaded_file = st.file_uploader("Choose an image", type=['png','jpg','jpeg'])
        if uploaded_file:
            img = Image.open(uploaded_file)
            st.image(img, width=500)
            predict_image(img)
