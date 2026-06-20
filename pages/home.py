import streamlit as st


@st.dialog("About the Models", width="large", icon=":material/info:")
def about_dialog():
    st.markdown("### Model Information")
    st.markdown("This system uses four different machine learning models for disease prediction:")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        **Heart Disease**
        - Algorithm: Logistic Regression
        - Features: 13 clinical parameters
        - Dataset: UCI Heart Disease dataset
        """)

        st.markdown("""
        **Pneumonia Detection**
        - Algorithm: VGG16 Convolutional Neural Network
        - Input: Chest X-ray images (224x224)
        - Classes: Normal, Pneumonia
        """)

    with col2:
        st.markdown("""
        **Skin Cancer**
        - Algorithm: Custom CNN
        - Input: Skin lesion images (28x28)
        - Classes: 7 lesion types (AKIEC, BCC, BKL, DF, NV, VASC, MEL)
        """)

        st.markdown("""
        **Multidisease**
        - Algorithm: Multinomial Naive Bayes
        - Features: 132 symptom binary indicators
        - Classes: 41 diseases
        """)

    st.divider()
    st.caption(
        "All models are trained on publicly available medical datasets. "
        "Predictions are approximate and intended for educational purposes only."
    )


st.markdown("""
<div class="page-header">
    <h2>Web-based Disease Prediction System</h2>
    <p>AI-powered health screening tools for early detection</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="info-box">
    Select a prediction tool from the navigation bar above to get started. Each tool uses
    machine learning models trained on medical datasets to provide preliminary screenings.
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-card-icon">🫀</div>
        <h3>Heart Disease</h3>
        <p style="color: #a3a8b4; font-size: 0.9rem;">
            Predicts heart disease risk using 13 clinical parameters including age,
            blood pressure, cholesterol levels, and ECG results.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-card">
        <div class="feature-card-icon">🔬</div>
        <h3>Pneumonia Detection</h3>
        <p style="color: #a3a8b4; font-size: 0.9rem;">
            Analyzes chest X-ray images to detect pneumonia using a VGG16 deep learning model.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-card-icon">🩺</div>
        <h3>Skin Cancer</h3>
        <p style="color: #a3a8b4; font-size: 0.9rem;">
            Classifies skin lesions into 7 types including melanoma and basal cell carcinoma.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-card">
        <div class="feature-card-icon">📋</div>
        <h3>Multidisease</h3>
        <p style="color: #a3a8b4; font-size: 0.9rem;">
            Matches your symptoms against 41 possible diseases using Naive Bayes classification.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("")

if st.button(":material/info: About the Models", use_container_width=False):
    about_dialog()

st.markdown("""
<div class="disclaimer" style="margin-top: 1rem;">
    **Important:** All predictions are approximate and based on statistical models.
    This system is intended for educational and informational purposes only.
    Always consult a qualified healthcare professional for medical decisions.
</div>
""", unsafe_allow_html=True)
