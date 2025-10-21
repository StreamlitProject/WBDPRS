import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

def heart():
    url = 'https://drive.google.com/uc?id=155zmtpJU3_uxcl1BGRRScgrgvKcswHdt'
    df = pd.read_csv(url)

    scaler = StandardScaler()
    scale_cols = ['age','trestbps','chol','thalach','oldpeak']
    df[scale_cols] = scaler.fit_transform(df[scale_cols])

    X = df.drop(['target'], axis=1)
    y = df['target']
    model = LogisticRegression()
    model.fit(X, y)

    st.info("Enter the following details for Heart Disease Prediction")
    form = st.form("Heart Disease Form")

    age = form.number_input("Age", min_value=1, max_value=120, value=30)
    sex = form.radio("Gender", ['Male','Female'])
    sex = 1 if sex=='Male' else 0
    cp = form.selectbox("Chest Pain Type", [1,2,3,4])
    trestbps = form.number_input("Resting BP")
    chol = form.number_input("Serum Cholesterol")
    fbs = form.radio("Fasting blood sugar >= 120 mg/dl?", [0,1])
    restecg = form.selectbox("Resting ECG", [0,1,2])
    thalach = form.number_input("Max Heart Rate")
    exang = form.radio("Exercise induced angina?", [0,1])
    oldpeak = form.number_input("ST depression induced by exercise")
    slope = form.selectbox("Slope of peak exercise ST segment", [1,2,3])
    ca = form.selectbox("Number of major vessels", [0,1,2,3])
    thal = form.selectbox("Defect type", [3,6,7])

    submitted = form.form_submit_button("Submit")
    if submitted:
        input_df = pd.DataFrame([[age, sex, cp, trestbps, chol, fbs, restecg, thalach,
                                  exang, oldpeak, slope, ca, thal]], columns=X.columns)
        pred = model.predict(input_df)[0]
        if pred==1:
            st.error("HIGH risk of Heart Disease!")
        else:
            st.success("LOW risk of Heart Disease!")
