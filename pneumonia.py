import streamlit as st
import numpy as np
from keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

def pneumonia():
    st.header("Pneumonia Detection")
    st.info("Approximate Pneumonia prediction (under development).")

    model = load_model("model_vgg16.h5")

    input_type = st.radio("Input Method:", ["Camera", "Upload Image"], horizontal=True, key="pneumonia_radio")

    def predict(img):
        img = img.resize((224,224)).convert("RGB")
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)/255.0
        pred = model.predict(x)
        label = "Normal" if np.argmax(pred[0])==0 else "Pneumonia"
        st.success(f"Prediction: {label}")

    if input_type=="Camera":
        pic = st.camera_input("Take Picture", key="pneumonia_camera")
        if pic:
            img = Image.open(pic)
            st.image(img, width=300)
            predict(img)
    else:
        upload = st.file_uploader("Upload X-ray", type=["jpg","png","jpeg"], key="pneumonia_upload")
        if upload:
            img = Image.open(upload)
            st.image(img, width=300)
            predict(img)
