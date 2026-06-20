import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


@st.cache_resource
def load_pneumonia_model():
    from keras.models import load_model
    return load_model("model_vgg16.h5")


def predict_image(model, img):
    from tensorflow.keras.preprocessing import image
    from keras.applications.vgg16 import preprocess_input
    img = img.resize((224, 224)).convert("RGB")
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    classes = model.predict(x)
    return classes[0]


st.markdown("""
<div class="page-header">
    <h2>Pneumonia Detection</h2>
    <p>Upload or capture a chest X-ray image for pneumonia screening</p>
</div>
""", unsafe_allow_html=True)

with st.popover("💡 How it works"):
    st.markdown("""
    The VGG16 deep learning model analyzes your chest X-ray
    and classifies it as either Normal or showing signs of Pneumonia.

    **Model:** VGG16 CNN (pretrained on ImageNet)
    **Input:** Chest X-ray images resized to 224x224
    **Output:** Probability scores for Normal and Pneumonia classes
    """)

try:
    with st.spinner("Loading pneumonia model..."):
        model = load_pneumonia_model()
    st.badge("VGG16 CNN", color="blue")
    model_ready = True
except Exception as e:
    st.error(f"Failed to load pneumonia model: {e}")
    st.stop()

tab_camera, tab_upload = st.tabs(["📷 Camera", "📁 Upload Image"])

def display_result(an_image):
    img_col, result_col = st.columns([1, 1])

    with img_col:
        st.image(an_image, caption="Analyzing image", use_column_width=True)

    with result_col:
        with st.spinner("Analyzing X-ray..."):
            probs = predict_image(model, an_image)

        normal_prob = float(probs[0])
        pneumonia_prob = float(probs[1])
        predicted_class = "Normal" if normal_prob > pneumonia_prob else "Pneumonia"
        confidence = max(normal_prob, pneumonia_prob)

        if predicted_class == "Pneumonia":
            st.markdown("""
            <div class="result-card positive">
                <div class="result-label">Diagnosis</div>
                <div class="result-value danger">Pneumonia Detected</div>
            </div>
            """, unsafe_allow_html=True)
            st.error("Please seek medical attention immediately.")
        else:
            st.markdown("""
            <div class="result-card negative">
                <div class="result-label">Diagnosis</div>
                <div class="result-value success">Normal</div>
            </div>
            """, unsafe_allow_html=True)
            st.balloons()

        st.progress(int(confidence * 100) / 100, text=f"Confidence: {confidence:.1%}")

        prob_df = pd.DataFrame({
            "Class": ["Normal", "Pneumonia"],
            "Probability": [normal_prob, pneumonia_prob],
        }).set_index("Class")
        st.bar_chart(prob_df, horizontal=True, height=120, color="#0f9b8e")

    st.toast("Pneumonia analysis complete!", icon="🔬")

    if "history" not in st.session_state:
        st.session_state.history = []
    st.session_state.history.append({
        "Module": "Pneumonia",
        "Result": predicted_class,
        "Confidence": f"{confidence:.1%}",
    })

    with st.expander("View details"):
        c1, c2, c3 = st.columns(3)
        c1.metric("Diagnosis", predicted_class)
        c2.metric("Confidence", f"{confidence:.1%}")
        c3.metric("Model", "VGG16")

    st.markdown("---")
    st.markdown("**Was this analysis helpful?**")
    feedback = st.feedback("faces")
    if feedback is not None:
        st.session_state.history[-1]["Rating"] = f"{feedback}/2"
        st.toast("Thanks for your feedback!", icon="⭐")

with tab_camera:
    picture = st.camera_input("📷 Capture a chest X-ray image")
    if picture is not None:
        an_image = Image.open(picture)
        display_result(an_image)

with tab_upload:
    uploaded_file = st.file_uploader("📁 Upload a chest X-ray image", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        an_image = Image.open(uploaded_file)
        display_result(an_image)
