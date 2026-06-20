import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


@st.cache_resource
def load_skin_model():
    from keras.models import load_model
    return load_model("best_model.h5")


SKIN_CLASSES = {
    0: "AKIEC", 1: "BCC", 2: "BKL", 3: "DF",
    4: "NV", 5: "VASC", 6: "MEL",
}

SKIN_DESCRIPTIONS = {
    "AKIEC": "Actinic keratoses and intraepithelial carcinoma. Pre-cancerous skin growths from sun damage.",
    "BCC": "Basal cell carcinoma. The most common and treatable form of skin cancer.",
    "BKL": "Benign keratosis. Non-cancerous skin growths, often age-related.",
    "DF": "Dermatofibroma. A benign skin growth, usually on lower legs.",
    "NV": "Melanocytic nevi. Common moles, generally harmless.",
    "VASC": "Vascular lesions. Blood vessel-related skin growths.",
    "MEL": "Melanoma. The most dangerous form of skin cancer. Seek medical attention.",
}

SKIN_RISK = {
    "MEL": "high", "BCC": "medium", "AKIEC": "medium",
    "NV": "low", "BKL": "low", "DF": "low", "VASC": "low",
}


def predict_skin(model, img):
    img = img.resize((28, 28)).convert("RGB")
    img_array = np.array(img).reshape(-1, 28, 28, 3)
    result = model.predict(img_array)
    probs = result[0].tolist()
    class_index = probs.index(max(probs))
    return class_index, probs


st.markdown("""
<div class="page-header">
    <h2>Skin Cancer Detection</h2>
    <p>Upload or capture a skin lesion image for lesion type classification</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="info-box">
    💡 **How it works:** A CNN model classifies your skin lesion image into one of
    7 types. Malignant types (Melanoma, BCC) are flagged with higher risk alerts.
</div>
""", unsafe_allow_html=True)

try:
    with st.spinner("Loading skin cancer model..."):
        model = load_skin_model()
    st.badge("Custom CNN", color="blue")
except Exception as e:
    st.error(f"Failed to load skin cancer model: {e}")
    st.stop()

tab_camera, tab_upload = st.tabs(["📷 Camera", "📁 Upload Image"])

def display_result(an_image):
    img_col, result_col = st.columns([1, 1])

    with img_col:
        st.image(an_image, caption="Analyzing image", use_column_width=True)

    with result_col:
        with st.spinner("Analyzing skin lesion..."):
            class_index, probs = predict_skin(model, an_image)

        label = SKIN_CLASSES[class_index]
        confidence = max(probs)
        risk = SKIN_RISK.get(label, "low")

        if risk in ("high", "medium"):
            border_class = "positive"
            value_class = "danger"
        else:
            border_class = "negative"
            value_class = "success"

        st.markdown(f"""
        <div class="result-card {border_class}">
            <div class="result-label">Lesion Type</div>
            <div class="result-value {value_class}">{label}</div>
            <div style="color: #a3a8b4; font-size: 0.85rem; margin-top: 0.3rem;">{SKIN_DESCRIPTIONS.get(label, '')}</div>
        </div>
        """, unsafe_allow_html=True)

        st.progress(int(confidence * 100) / 100, text=f"Confidence: {confidence:.1%}")

        prob_df = pd.DataFrame({
            "Type": list(SKIN_CLASSES.values()),
            "Probability": probs,
        }).set_index("Type")
        st.bar_chart(prob_df, horizontal=True, height=200, color="#0f9b8e")

    if risk == "high":
        st.error("⚠️ **High-risk lesion detected.** Please consult a dermatologist immediately.")
    elif risk == "medium":
        st.warning("⚠️ **Medium-risk lesion detected.** Consider scheduling a dermatology appointment.")
    else:
        st.success("Low-risk lesion. Regular monitoring is recommended.")
        st.balloons()

    st.toast("Skin lesion analysis complete!", icon="🩺")

    if "history" not in st.session_state:
        st.session_state.history = []
    st.session_state.history.append({
        "Module": "Skin Cancer",
        "Result": f"{label} ({risk})",
        "Confidence": f"{confidence:.1%}",
    })

    with st.expander("View details"):
        c1, c2, c3 = st.columns(3)
        c1.metric("Lesion Type", label)
        c2.metric("Confidence", f"{confidence:.1%}")
        c3.metric("Risk Level", risk.capitalize())

with tab_camera:
    picture = st.camera_input("📷 Capture a skin lesion image")
    if picture is not None:
        an_image = Image.open(picture)
        display_result(an_image)

with tab_upload:
    uploaded_file = st.file_uploader("📁 Upload a skin lesion image", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        an_image = Image.open(uploaded_file)
        display_result(an_image)
