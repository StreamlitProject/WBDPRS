import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


@st.cache_resource
def load_data_and_model():
    url = "https://drive.google.com/uc?id=155zmtpJU3_uxcl1BGRRScgrgvKcswHdt"
    df = pd.read_csv(url)

    X = df.drop(["target"], axis=1)
    y = df["target"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=40)

    scaler = StandardScaler()
    columns_to_scale = ["age", "trestbps", "chol", "thalach", "oldpeak"]
    X_train[columns_to_scale] = scaler.fit_transform(X_train[columns_to_scale])
    X_test[columns_to_scale] = scaler.transform(X_test[columns_to_scale])

    lr = LogisticRegression()
    model = lr.fit(X_train, y_train)
    return model, scaler


st.markdown("""
<div class="page-header">
    <h2>Heart Disease Prediction</h2>
    <p>Enter your clinical parameters to assess heart disease risk</p>
</div>
""", unsafe_allow_html=True)

try:
    with st.spinner("Loading model..."):
        model, scaler = load_data_and_model()
    st.badge("Logistic Regression", color="blue")
except Exception as e:
    st.error(f"Failed to load heart disease model: {e}")
    st.stop()

with st.form("heart_form"):
    c1, c2 = st.columns(2)

    with c1:
        st.markdown("**Demographics**")
        age = st.number_input(
            "Age", min_value=1, max_value=120, value=45,
            help="Normal range: 20-80 years"
        )
        sex = st.radio("Gender", ["Male", "Female"], horizontal=True)

        st.markdown("**Vitals**")
        trestbps = st.number_input(
            "Resting blood pressure (mmHg)", min_value=60, max_value=250, value=120,
            help="Normal: <120 mmHg"
        )
        chol = st.number_input(
            "Serum cholesterol (mg/dL)", min_value=100, max_value=600, value=200,
            help="Desirable: <200 mg/dL"
        )
        fbs = st.radio("Fasting blood sugar > 120 mg/dL?", ["No", "Yes"], horizontal=True)

    with c2:
        st.markdown("**ECG & Exercise**")
        cp = st.selectbox("Chest pain type", [
            "Typical angina",
            "Atypical angina",
            "Non-anginal pain",
            "Asymptomatic",
        ])
        restecg = st.selectbox("Resting ECG results", [
            "Normal",
            "ST-T wave abnormality",
            "Left ventricular hypertrophy",
        ])
        thalach = st.number_input(
            "Max heart rate achieved", min_value=60, max_value=220, value=150,
            help="Normal during exercise: 100-170 bpm"
        )
        exang = st.radio("Exercise-induced angina?", ["No", "Yes"], horizontal=True)

        st.markdown("**Additional**")
        oldpeak = st.number_input(
            "ST depression (exercise vs rest)", min_value=0.0, max_value=10.0, value=0.0, step=0.1,
            help="Normal: 0. Higher values indicate abnormality."
        )
        slope = st.selectbox("Peak exercise ST slope", [
            "Upsloping",
            "Flat",
            "Downsloping",
        ])
        ca = st.slider("Major vessels colored by fluoroscopy", 0, 3, 0,
                        help="0 = normal, 3 = severe")
        thal = st.selectbox("Thalassemia type", [
            "Normal",
            "Fixed defect",
            "Reversible defect",
        ])

    submitted = st.form_submit_button("Predict Heart Disease Risk", use_container_width=True)

if submitted:
    with st.spinner("Analyzing your results..."):
        CP_MAP = {"Typical angina": 1, "Atypical angina": 2, "Non-anginal pain": 3, "Asymptomatic": 4}
        RESTECG_MAP = {"Normal": 0, "ST-T wave abnormality": 1, "Left ventricular hypertrophy": 2}
        SLOPE_MAP = {"Upsloping": 1, "Flat": 2, "Downsloping": 3}
        THAL_MAP = {"Normal": 3, "Fixed defect": 6, "Reversible defect": 7}

        sex_val = 1 if sex == "Male" else 0
        fbs_val = 1 if fbs == "Yes" else 0
        exang_val = 1 if exang == "Yes" else 0

        columns = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
                    "thalach", "exang", "oldpeak", "slope", "ca", "thal"]
        raw = np.array([[
            age, sex_val, CP_MAP[cp], trestbps, chol, fbs_val,
            RESTECG_MAP[restecg], thalach, exang_val, oldpeak,
            SLOPE_MAP[slope], ca, THAL_MAP[thal],
        ]])
        input_df = pd.DataFrame(raw, columns=columns)

        columns_to_scale = ["age", "trestbps", "chol", "thalach", "oldpeak"]
        input_df[columns_to_scale] = scaler.transform(input_df[columns_to_scale])

        prediction = model.predict(input_df)
        prob = model.predict_proba(input_df)[0]

    is_high_risk = prediction[0] == 1
    risk_pct = int(prob[1] * 100 if is_high_risk else prob[0] * 100)

    if is_high_risk:
        st.markdown("""
        <div class="result-card positive">
            <div class="result-label">Prediction Result</div>
            <div class="result-value danger">High Risk of Heart Disease</div>
        </div>
        """, unsafe_allow_html=True)
        st.progress(risk_pct / 100, text=f"Risk probability: {risk_pct}%")
        st.warning("Please consult a cardiologist for a thorough evaluation.")
    else:
        st.markdown("""
        <div class="result-card negative">
            <div class="result-label">Prediction Result</div>
            <div class="result-value success">Low Risk of Heart Disease</div>
        </div>
        """, unsafe_allow_html=True)
        st.progress(risk_pct / 100, text=f"Confidence: {risk_pct}%")
        st.success("Maintain a healthy lifestyle for continued well-being.")
        st.balloons()

    st.toast("Heart disease prediction complete!", icon="🫀")

    if "history" not in st.session_state:
        st.session_state.history = []
    st.session_state.history.append({
        "Module": "Heart Disease",
        "Result": "High Risk" if is_high_risk else "Low Risk",
        "Confidence": f"{max(prob) * 100:.1f}%",
    })

    with st.expander("View prediction details"):
        c1, c2, c3 = st.columns(3)
        c1.metric("Prediction", "High Risk" if is_high_risk else "Low Risk")
        c2.metric("Risk Probability", f"{risk_pct}%")
        c3.metric("Confidence", f"{max(prob) * 100:.1f}%")

    st.markdown("---")
    st.markdown("**Was this prediction helpful?**")
    feedback = st.feedback("faces")
    if feedback is not None:
        st.session_state.history[-1]["Rating"] = f"{feedback}/2"
        st.toast("Thanks for your feedback!", icon="⭐")
