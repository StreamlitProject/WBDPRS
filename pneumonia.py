import streamlit as st
import numpy as np
from PIL import Image
from keras.models import load_model
from tensorflow.keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input

def pneumonia():
    st.info("Upload or capture your chest X-ray to predict Pneumonia.")

    model = load_model('model_vgg16.h5')

    input_type = st.radio(
        "Select Input Method",
        ['Camera', 'Upload Image'],
        horizontal=True,
        key="pneu_input_type"
    )

    def predict_image(img):
        img = img.resize((224,224)).convert('RGB')
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        pred = model.predict(x)
        if pred.shape[1] == 2:
            idx = np.argmax(pred[0])
            st.success("Normal" if idx==0 else "Pneumonia")
        else:
            st.warning("Unexpected model output")

    if input_type == 'Camera':
        picture = st.camera_input("Take a picture", key="pneu_camera")
        if picture:
            img = Image.open(picture)
            st.image(img, width=400)
            predict_image(img)
    elif input_type == 'Upload Image':
        uploaded_file = st.file_uploader(
            "Choose a file", 
            type=['png','jpg','jpeg'],
            key="pneu_upload"
        )
        if uploaded_file:
            img = Image.open(uploaded_file)
            st.image(img, width=400)
            predict_image(img)
