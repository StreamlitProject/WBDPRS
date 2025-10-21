import streamlit as st
import numpy as np
from keras.models import load_model
from tensorflow.keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from PIL import Image

def pneumonia():
    st.markdown("## Have a Quick Overlook :eyes:")
    st.text("Step I: Scroll down to check whether you have Pneumonia or not.")
    st.text("Step II: Choose either Camera input or Upload Image to provide an X-ray image.")
    st.text("Step III: Click Submit to see the prediction.\n")
    st.markdown("That's cool :sunglasses:")
    st.info("Note: This is an approximate model under development.")

    model = load_model('model_vgg16.h5')

    selected_input = st.radio("Select Input Method", ['Camera', 'Upload Image'], horizontal=True)

    def predict_image(img):
        img = img.resize((224,224)).convert('RGB')
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        classes = model.predict(x)
        pred_idx = int(np.argmax(classes[0]))
        st.success("Normal" if pred_idx==0 else "Pneumonia")

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
