import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

def heart():
    st.markdown("## Heart Disease Risk Checker :heart:")
    st.info("Fill the form to estimate risk of heart disease.")

    url = 'https://drive.google.com/uc?id=155zmtpJU3_uxcl1BGRRScgrgvKcswHdt'
    df = pd.read_csv(url)
    scaler = StandardScaler()
    for col in ['age','trestbps','chol','thalach','oldpeak']:
        df[col] = scaler.fit_transform(df[[col]])

    X = df.drop(['target'], axis=1)
    y = df['target']
    model = LogisticRegression().fit(X, y)

    form = st.form(key="Heart")
    age = form.number_input("Age", 1,120,30)
    sex = form.radio("Gender", ['Male','Female'], horizontal=True)
    sex_val = 1 if sex=='Male' else 0
    cp = form.radio("Chest Pain Type", ['Typical','Atypical','Non-angina','Asymptomatic'], horizontal=True)
    cp_val = ['Typical','Atypical','Non-angina','Asymptomatic'].index(cp)+1
    trestbps = form.number_input("Resting BP")
    chol = form.number_input("Cholesterol")
    fbs = form.radio("Fasting Blood Sugar >=120 mg/dL", ['Yes','No'], horizontal=True)
    fbs_val = 1 if fbs=='Yes' else 0
    thalach = form.number_input("Max Heart Rate")
    exang = form.radio("Exercise Induced Angina", ['Yes','No'], horizontal=True)
    exang_val = 1 if exang=='Yes' else 0
    oldpeak = form.number_input("ST Depression")
    submit = form.form_submit_button("Submit")

    if submit:
        data = pd.DataFrame([[age, sex_val, cp_val, trestbps, chol, fbs_val, thalach, exang_val, oldpeak]], columns=X.columns[:9])
        pred = model.predict(data)[0]
        if pred==1:
            st.error("HIGH risk of heart disease")
        else:
            st.success("LOW risk of heart disease")
