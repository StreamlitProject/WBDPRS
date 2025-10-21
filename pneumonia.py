import streamlit as st
import numpy as np
from keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

def pneumonia():
    st.info("Approximate Pneumonia prediction (under development).")

    # Load model
    model = load_model("model_vgg16.h5")

    # Input type
    input_type = st.radio(
        "Input Method:",
        ["Camera", "Upload Image"],
        horizontal=True,
        key="pneumonia_input"
    )

    def predict_image(img):
        img = img.resize((224, 224)).convert("RGB")
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = x / 255.0
        result = model.predict(x)
        if result.shape[1] == 2:
            pred_idx = np.argmax(result[0])
            st.success("Prediction: " + ("Normal" if pred_idx == 0 else "Pneumonia"))
        else:
            st.warning("Unexpected model output")

    # Camera input
    if input_type == "Camera":
        pic = st.camera_input("Take a picture", key="pneumonia_camera")
        if pic:
            img = Image.open(pic)
            st.image(img, width=300)
            predict_image(img)

    # Upload
    if input_type == "Upload Image":
        file = st.file_uploader("Upload X-ray image", type=["png", "jpg", "jpeg"], key="pneumonia_upload")
        if file:
            img = Image.open(file)
            st.image(img, width=300)
            predict_image(img)
