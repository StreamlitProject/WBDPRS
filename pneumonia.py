import streamlit as st
import numpy as np
from keras.models import load_model
from tensorflow.keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from PIL import Image

def pneumonia():
    st.markdown("## Pneumonia Prediction :lungs:")
    st.info("Upload a chest X-ray image or use your camera to detect Pneumonia. Approximate model under development.")

    model = load_model(r'model_vgg16.h5')

    # Input method
    input_method = st.radio("Select Input Method", ["Camera", "Upload Image"], horizontal=True, key="pneu_input")

    def predict_image(img):
        img = img.resize((224,224)).convert('RGB')
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        result = model.predict(x)
        pred_idx = int(np.argmax(result[0]))
        if result.shape[1]==2:
            if pred_idx == 0:
                st.success("Prediction: Normal")
            else:
                st.error("Prediction: Pneumonia")
        else:
            st.warning("Unexpected model output shape.")

    # Camera
    if input_method == "Camera":
        picture = st.camera_input("Take a picture", key="pneu_cam")
        if picture is not None:
            img = Image.open(picture)
            st.image(img, width=400)
            predict_image(img)

    # Upload
    else:
        uploaded_file = st.file_uploader("Upload image", type=["jpg","jpeg","png"], key="pneu_file")
        if uploaded_file is not None:
            img = Image.open(uploaded_file)
            st.image(img, width=400)
            predict_image(img)
