import streamlit as st
import numpy as np
from keras.models import load_model
from PIL import Image

def skin():
    st.markdown("## Skin Cancer Prediction :microscope:")
    st.info("Upload a skin lesion image or use your camera to predict the type of lesion. Approximate model under development.")

    model = load_model(r'best_model.h5')

    # Input selection
    input_method = st.radio("Select Input Method", ["Camera", "Upload Image"], horizontal=True, key="skin_input")

    # Function to predict
    def predict_image(img):
        img = img.resize((28,28)).convert('RGB')
        img_array = np.array(img).reshape(-1,28,28,3)
        result = model.predict(img_array)
        class_index = int(np.argmax(result[0]))
        classes = {
            0: 'Akiec : Actinic keratoses and intraepithelial carcinoma',
            1: 'Bcc : Basal cell carcinoma',
            2: 'Bkl : Benign lesions of the keratosis',
            3: 'Df : Dermatofibroma',
            4: 'Nv : Melanocytic nevi',
            5: 'Vasc : Vascular lesions',
            6: 'Mel : Melanoma'
        }
        st.success(classes[class_index])

    # Camera input
    if input_method == "Camera":
        picture = st.camera_input("Take a picture", key="skin_cam")
        if picture is not None:
            img = Image.open(picture)
            st.image(img, width=400)
            predict_image(img)

    # Upload input
    else:
        uploaded_file = st.file_uploader("Upload image", type=["jpg","jpeg","png"], key="skin_file")
        if uploaded_file is not None:
            img = Image.open(uploaded_file)
            st.image(img, width=400)
            predict_image(img)
