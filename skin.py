import streamlit as st
import numpy as np
from keras.models import load_model
from PIL import Image

def skin():
    st.header("Skin Lesion Prediction")
    st.info("Approximate skin lesion prediction (under development).")

    model = load_model("best_model.h5")

    input_type = st.radio("Input Method:", ["Camera", "Upload Image"], horizontal=True, key="skin_radio")

    classes = {
        0: 'Akiec', 1: 'Bcc', 2: 'Bkl', 3: 'Df', 4: 'Nv', 5: 'Vasc', 6: 'Mel'
    }

    def predict_image(img):
        img = img.resize((28, 28)).convert("RGB")
        arr = np.array(img).reshape(-1,28,28,3)
        pred = model.predict(arr)
        st.success(f"Prediction: {classes[int(np.argmax(pred[0]))]}")

    if input_type == "Camera":
        pic = st.camera_input("Take Picture", key="skin_camera")
        if pic:
            img = Image.open(pic)
            st.image(img, width=300)
            predict_image(img)
    else:
        upload = st.file_uploader("Upload Image", type=["jpg","png","jpeg"], key="skin_upload")
        if upload:
            img = Image.open(upload)
            st.image(img, width=300)
            predict_image(img)
