import streamlit as st
import numpy as np
from keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

def pneumonia():
    st.markdown("## Pneumonia Detection from X-ray")
    st.info("Approximate predictions using an AI model. For demonstration purposes only.")

    model = load_model('model_vgg16.h5')

    input_type = st.radio("Input Method:", ["Camera", "Upload Image"], horizontal=True)

    def predict_image(img):
        img = img.resize((224,224)).convert('RGB')
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = x/255.0  # normalize
        classes = model.predict(x)
        if classes.shape[1]==2:
            st.success("Pneumonia" if np.argmax(classes[0]) else "Normal")
        else:
            st.warning("Unexpected model output.")

    if input_type == "Camera":
        picture = st.camera_input("Take a picture")
        if picture:
            img = Image.open(picture)
            st.image(img, width=400)
            predict_image(img)
    else:
        uploaded_file = st.file_uploader("Upload Image", type=['png','jpg','jpeg'])
        if uploaded_file:
            img = Image.open(uploaded_file)
            st.image(img, width=400)
            predict_image(img)
