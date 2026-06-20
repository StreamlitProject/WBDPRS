import streamlit as st


@st.dialog("About the Models")
def about_models_dialog():
    st.markdown("### Model Information")

    c1, c2 = st.columns(2)

    with c1:
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

    with c2:
        st.markdown("""
        **Skin Cancer**
        - Algorithm: Custom CNN
        - Input: Skin lesion images (28x28)
        - Classes: 7 lesion types
        """)

        st.markdown("""
        **Multidisease**
        - Algorithm: Multinomial Naive Bayes
        - Features: 132 symptom indicators
        - Classes: 41 diseases
        """)

    st.divider()
    st.caption(
        "All models are trained on publicly available medical datasets. "
        "Predictions are approximate and intended for educational purposes only."
    )


logo_col1, logo_col2, logo_col3 = st.columns([1, 1, 1])
with logo_col2:
    st.image("assets/logo.svg", width=100, use_container_width=False)

st.markdown("""
<div class="page-header">
    <h2>HealthPulse</h2>
    <p>AI-powered health screening tools for early detection</p>
</div>
""", unsafe_allow_html=True)

cards = [
    ("🫀", "Heart Disease", "Predicts heart disease risk using 13 clinical parameters including age, blood pressure, cholesterol, and ECG results.", "pages/heart.py"),
    ("🔬", "Pneumonia Detection", "Analyzes chest X-ray images to detect pneumonia using a VGG16 deep learning model.", "pages/pneumonia.py"),
    ("🩺", "Skin Cancer", "Classifies skin lesions into 7 types including melanoma and basal cell carcinoma.", "pages/skin.py"),
    ("📋", "Multidisease", "Matches your symptoms against 41 possible diseases using Naive Bayes classification.", "pages/multidisease.py"),
]

col1, col2 = st.columns(2)
cols = [col1, col2]

for i, (icon, title, desc, page) in enumerate(cards):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="feature-card" style="cursor: pointer;">
            <div class="feature-card-icon">{icon}</div>
            <h3>{title}</h3>
            <p style="color: #a3a8b4; font-size: 0.88rem; line-height: 1.5;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"Open {title}", key=f"btn_{i}", use_container_width=True):
            st.switch_page(page)

st.markdown("")

if st.session_state.get("history"):
    st.markdown("---")
    st.markdown("### Recent Predictions")

    history_data = st.session_state.history[-10:][::-1]
    for i, entry in enumerate(history_data):
        result = entry.get("Result", "")
        confidence = entry.get("Confidence", "")
        module = entry.get("Module", "")
        rating = entry.get("Rating", "")

        if "High" in result or "Detected" in result or "high" in entry.get("Result", "").lower():
            badge_class = "danger"
        elif "Low" in result or "Normal" in result or "low" in entry.get("Result", "").lower():
            badge_class = "success"
        else:
            badge_class = "warning"

        st.markdown(f"""
        <div class="history-item">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <span style="font-weight: 600; color: #fafafa;">{module}</span>
                    <span class="history-badge {badge_class}" style="margin-left: 0.5rem;">{result}</span>
                </div>
                <div style="color: #a3a8b4; font-size: 0.85rem;">
                    {confidence} {f'| {rating}' if rating else ''}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

c1, c2, c3 = st.columns([1, 1, 1])
with c2:
    if st.button("About the Models", use_container_width=True):
        about_models_dialog()

st.markdown("""
<div class="disclaimer" style="margin-top: 1rem;">
    **Important:** All predictions are approximate and based on statistical models.
    This system is intended for educational and informational purposes only.
    Always consult a qualified healthcare professional for medical decisions.
</div>
""", unsafe_allow_html=True)
