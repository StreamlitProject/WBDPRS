import streamlit as st
import numpy as np
from keras.models import load_model
from PIL import Image

def skin():
    st.info("Approximate skin lesion prediction (under development).")

    # Load model
    model = load_model("best_model.h5")

    # Input selection
    input_type = st.radio(
        "Select Input Method:",
        ["Camera", "Upload Image"],
        horizontal=True,
        key="skin_input"
    )

    # Class mapping
    classes = {
        0: 'Akiec : Actinic keratoses',
        1: 'Bcc : Basal cell carcinoma',
        2: 'Bkl : Benign keratosis',
        3: 'Df : Dermatofibroma',
        4: 'Nv : Melanocytic nevi',
        5: 'Vasc : Vascular lesions',
        6: 'Mel : Melanoma'
    }

    def predict_image(img):
        img = img.resize((28, 28)).convert("RGB")
        img_array = np.array(img).reshape(-1, 28, 28, 3)
        result = model.predict(img_array)
        class_index = int(np.argmax(result[0]))
        st.success(f"Prediction: {classes[class_index]}")

    # Camera input
    if input_type == "Camera":
        picture = st.camera_input("Take a picture", key="skin_camera")
        if picture:
            img = Image.open(picture)
            st.image(img, width=300)
            predict_image(img)

    # Upload image
    if input_type == "Upload Image":
        uploaded_file = st.file_uploader(
            "Upload an image", type=["png", "jpg", "jpeg"], key="skin_upload"
        )
        if uploaded_file:
            img = Image.open(uploaded_file)
            st.image(img, width=300)
            predict_image(img)
