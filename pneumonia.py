import streamlit as st
import numpy as np
from keras.models import load_model
from tensorflow.keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from PIL import Image

def pneumonia():
    st.markdown("## Pneumonia X-ray Checker :microscope:")
    st.info("Upload or take a chest X-ray. Approximate results only!")

    model = load_model("model_vgg16.h5")

    input_type = st.radio("Select Input Method", ['Camera', 'Upload Image'], horizontal=True)

    def predict(img):
        img = img.resize((224,224)).convert('RGB')
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        pred = model.predict(x)
        if pred.shape[1]==2:
            idx = int(np.argmax(pred[0]))
            st.success("Normal" if idx==0 else "Pneumonia")
        else:
            st.warning("Unexpected model output shape")

    if input_type == "Camera":
        pic = st.camera_input("Take a picture")
        if pic:
            img = Image.open(pic)
            st.image(img, width=400)
            predict(img)

    else:
        upload = st.file_uploader("Upload Image", type=['png','jpg','jpeg'])
        if upload:
            img = Image.open(upload)
            st.image(img, width=400)
            predict(img)
