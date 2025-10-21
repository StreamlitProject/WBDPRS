import streamlit as st
import numpy as np
from keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
from streamlit_extras.badges import badge

def pneumonia():
    st.info("Upload X-ray or use camera to predict Pneumonia.")

    model = load_model('model_vgg16.h5')
    cols = st.columns(2)
    with cols[0]:
        cam = st.camera_input("Take a picture", key="pneu_cam")
    with cols[1]:
        upload = st.file_uploader("Upload X-ray", type=['png','jpg','jpeg'], key="pneu_upload")

    img = cam or upload

    if img:
        img = Image.open(img)
        st.image(img, width=400)

        def predict(img):
            img = img.resize((224,224)).convert('RGB')
            x = image.img_to_array(img)/255.0
            x = np.expand_dims(x, axis=0)
            pred = model.predict(x)
            result = "Pneumonia" if np.argmax(pred[0]) else "Normal"
            st.success(f"Prediction: {result}")
            badge("🩺 Accuracy approx: 85%", color="green")

        predict(img)
