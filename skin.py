import streamlit as st
import numpy as np
from keras.models import load_model
from PIL import Image
from streamlit_extras.mention import mention

def skin():
    st.info("Upload an image or use your camera for Skin Lesion detection.")

    model = load_model('best_model.h5')

    cols = st.columns(2)
    with cols[0]:
        cam = st.camera_input("Take a picture", key="skin_cam")
    with cols[1]:
        upload = st.file_uploader("Upload Image", type=['png','jpg','jpeg'], key="skin_upload")

    img = cam or upload

    if img:
        image = Image.open(img)
        st.image(image, width=400)

        def predict(img):
            img = img.resize((28,28)).convert('RGB')
            arr = np.array(img).reshape(-1,28,28,3)
            pred = model.predict(arr)
            classes = ['Akiec','Bcc','Bkl','Df','Nv','Vasc','Mel']
            st.balloons()
            st.success(f"Prediction: {classes[int(np.argmax(pred[0]))]}")
            mention("Note: Model is approximate and under development.", icon="💡")

        predict(image)
