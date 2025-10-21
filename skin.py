import streamlit as st
import numpy as np
from keras.models import load_model
from PIL import Image

def skin():
    st.markdown("## Quick Skin Lesion Checker :eyes:")
    st.info("Upload or take a photo to predict the type of lesion. Approximate results only!")

    # Load model
    model = load_model("best_model.h5")

    # Input type selection
    input_type = st.radio("Select Input Method", ['Camera', 'Upload Image'], horizontal=True)

    # Class labels
    classes = {
        0: 'Akiec: Actinic keratoses',
        1: 'Bcc: Basal cell carcinoma',
        2: 'Bkl: Benign keratosis',
        3: 'Df: Dermatofibroma',
        4: 'Nv: Melanocytic nevi',
        5: 'Vasc: Vascular lesions',
        6: 'Mel: Melanoma'
    }

    def predict(img):
        img = img.resize((28,28)).convert('RGB')
        arr = np.array(img).reshape(-1,28,28,3)
        pred = model.predict(arr)
        idx = int(np.argmax(pred[0]))
        st.success(f"Predicted Lesion: {classes[idx]}")

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
