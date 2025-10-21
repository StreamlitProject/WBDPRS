import streamlit as st
import numpy as np
from keras.models import load_model
from PIL import Image

def skin():
    st.markdown("## Detect Your Skin Lesion")
    st.info("Approximate predictions using an AI model. For demonstration purposes only.")
    
    model = load_model('best_model.h5')  # Load once

    input_type = st.radio("Input Method:", ["Camera", "Upload Image"], horizontal=True)

    classes = {
        0: 'Akiec: Actinic keratoses', 1: 'Bcc: Basal cell carcinoma',
        2: 'Bkl: Benign keratosis', 3: 'Df: Dermatofibroma',
        4: 'Nv: Melanocytic nevi', 5: 'Vasc: Vascular lesions',
        6: 'Mel: Melanoma'
    }

    def predict_image(img):
        img = img.resize((28,28)).convert('RGB')
        img_array = np.array(img).reshape(-1,28,28,3)
        result = model.predict(img_array)
        st.success(classes[int(np.argmax(result[0]))])

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
