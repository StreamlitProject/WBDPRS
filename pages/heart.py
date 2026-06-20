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
    <p>Enter your clinical parameters below to assess heart disease risk</p>
</div>
""", unsafe_allow_html=True)

try:
    with st.spinner("Loading model..."):
        model, scaler = load_data_and_model()
    st.badge("Logistic Regression", color="blue")
except Exception as e:
    st.error(f"Failed to load heart disease model: {e}")
    st.stop()

with st.form("Heart Disease Prediction"):
    c1, c2 = st.columns(2)

    with c1:
        st.markdown("#### 👤 Demographics")
        age = st.number_input("Age (years)", min_value=1, max_value=120, value=45, help="Your age in complete years")
        sex = st.radio("Gender", ["Male", "Female"], horizontal=True)

        st.markdown("#### 🩸 Vitals")
        trestbps = st.number_input("Resting blood pressure (mmHg)", min_value=60, max_value=250, value=120,
                                   help="Blood pressure at rest, in mmHg. Normal: ~120/80")
        chol = st.number_input("Serum cholesterol (mg/dL)", min_value=100, max_value=600, value=200,
                               help="Total serum cholesterol. Desirable: <200 mg/dL")
        fbs = st.radio("Fasting blood sugar > 120 mg/dL?", ["No", "Yes"], horizontal=True,
                       help="Fasting blood sugar above 120 mg/dL indicates elevated glucose")

    with c2:
        st.markdown("#### ❤️ ECG & Exercise")
        cp = st.selectbox("Chest pain type", [
            "Typical angina (1)",
            "Atypical angina (2)",
            "Non-anginal pain (3)",
            "Asymptomatic (4)",
        ], help="Type of chest pain experienced")
        restecg = st.selectbox("Resting ECG results", [
            "Normal (0)",
            "ST-T wave abnormality (1)",
            "Left ventricular hypertrophy (2)",
        ], help="Resting electrocardiographic results")
        thalach = st.number_input("Max heart rate achieved", min_value=60, max_value=220, value=150,
                                  help="Maximum heart rate reached during exercise. Normal: 100-170")
        exang = st.radio("Exercise-induced angina?", ["No", "Yes"], horizontal=True,
                         help="Chest pain triggered by exercise")

        st.markdown("#### 🧪 Additional")
        oldpeak = st.number_input("ST depression (exercise vs rest)", min_value=0.0, max_value=10.0, value=0.0, step=0.1,
                                  help="ST segment depression induced by exercise. Normal: 0")
        slope = st.selectbox("Peak exercise ST slope", [
            "Upsloping (1)",
            "Flat (2)",
            "Downsloping (3)",
        ], help="Slope of the peak exercise ST segment")
        ca = st.slider("Major vessels colored by fluoroscopy", 0, 3, 0,
                        help="Number of major vessels (0-3) colored by fluoroscopy")
        thal = st.selectbox("Thalassemia type", [
            "Normal (3)",
            "Fixed defect (6)",
            "Reversible defect (7)",
        ], help="Thalassemia defect classification")

    submitted = st.form_submit_button("Predict Heart Disease Risk", use_container_width=True)

if submitted:
    with st.spinner("Analyzing your results..."):
        sex_val = 1 if sex == "Male" else 0
        cp_val = int(cp.split("(")[-1].replace(")", ""))
        fbs_val = 1 if fbs == "Yes" else 0
        restecg_val = int(restecg.split("(")[-1].replace(")", ""))
        exang_val = 1 if exang == "Yes" else 0
        slope_val = int(slope.split("(")[-1].replace(")", ""))
        ca_val = ca
        thal_val = int(thal.split("(")[-1].replace(")", ""))

        columns = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
                    "thalach", "exang", "oldpeak", "slope", "ca", "thal"]
        raw = np.array([[age, sex_val, cp_val, trestbps, chol, fbs_val,
                         restecg_val, thalach, exang_val, oldpeak, slope_val,
                         ca_val, thal_val]])
        input_df = pd.DataFrame(raw, columns=columns)

        columns_to_scale = ["age", "trestbps", "chol", "thalach", "oldpeak"]
        input_df[columns_to_scale] = scaler.transform(input_df[columns_to_scale])

        prediction = model.predict(input_df)
        prob = model.predict_proba(input_df)[0]

    if prediction[0] == 1:
        risk_pct = int(prob[1] * 100)
        st.markdown(f"""
        <div class="result-card positive">
            <div class="result-label">Prediction Result</div>
            <div class="result-value danger">High Risk of Heart Disease</div>
        </div>
        """, unsafe_allow_html=True)
        st.progress(risk_pct / 100, text=f"Risk probability: {risk_pct}%")
        st.warning("Please consult a cardiologist for a thorough evaluation.")
    else:
        risk_pct = int(prob[0] * 100)
        st.markdown(f"""
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
        "Result": "High Risk" if prediction[0] == 1 else "Low Risk",
        "Confidence": f"{max(prob) * 100:.1f}%",
    })

    with st.expander("View prediction details"):
        c1, c2, c3 = st.columns(3)
        c1.metric("Prediction", "High Risk" if prediction[0] == 1 else "Low Risk")
        c2.metric("Risk Probability", f"{risk_pct}%")
        c3.metric("Confidence", f"{max(prob) * 100:.1f}%")

    st.markdown("---")
    st.markdown("**Was this prediction helpful?**")
    feedback = st.feedback("faces")
    if feedback is not None:
        st.session_state.history[-1]["Rating"] = f"{feedback}/2"
        st.toast("Thanks for your feedback!", icon="⭐")
