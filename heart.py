import pandas as pd
import numpy as np
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

def heart():
    st.markdown("## Heart Disease Prediction ❤️")
    st.info("Provide your details to predict the risk of heart disease.")

    url = 'https://drive.google.com/uc?id=155zmtpJU3_uxcl1BGRRScgrgvKcswHdt'
    df = pd.read_csv(url)

    scaler = StandardScaler()
    scale_cols = ['age','trestbps','chol','thalach','oldpeak']
    df[scale_cols] = scaler.fit_transform(df[scale_cols])

    X = df.drop(['target'], axis=1)
    y = df['target']
    model = LogisticRegression()
    model.fit(X, y)

    form = st.form(key="heart_form")
    age = form.number_input("Age", min_value=1, max_value=120, value=30, key="heart_age")
    sex = form.radio("Gender", ('Male','Female'), key="heart_sex")
    sex_val = 1 if sex=='Male' else 0
    cp_map = {'1=typical angina':1, '2=atypical angina':2, '3=non-angina pain':3, '4=asymptomatic':4}
    cp = cp_map[form.radio("Chest pain type", tuple(cp_map.keys()), key="heart_cp")]
    trestbps = form.number_input("Resting BP", key="heart_bp")
    chol = form.number_input("Serum cholesterol", key="heart_chol")
    fbs = 1 if form.radio("Fasting blood sugar ≥120 mg/dL?", ('Yes','No'), key="heart_fbs")=='Yes' else 0
    restecg_map = {'0=normal':0,'1=ST-T abnormal':1,'2=LV hypertrophy':2}
    restecg = restecg_map[form.radio("Resting ECG", tuple(restecg_map.keys()), key="heart_ecg")]
    thalach = form.number_input("Max heart rate", key="heart_thalach")
    exang = 1 if form.radio("Exercise induced angina?", ('Yes','No'), key="heart_exang")=='Yes' else 0
    oldpeak = form.number_input("ST depression", key="heart_oldpeak")
    slope_map = {'1=unsloping':1,'2=flat':2,'3=downsloping':3}
    slope = slope_map[form.radio("Slope of ST segment", tuple(slope_map.keys()), key="heart_slope")]
    ca = int(form.radio("Number of major vessels colored", ('0','1','2','3'), key="heart_ca"))
    thal_map = {'3=normal':3,'6=fixed':6,'7=reversible defect':7}
    thal = thal_map[form.radio("Defect type", tuple(thal_map.keys()), key="heart_thal")]

    submitted = form.form_submit_button("Submit", key="heart_submit")

    if submitted:
        input_data = pd.DataFrame([[age, sex_val, cp, trestbps, chol, fbs, restecg, thalach,
                                    exang, oldpeak, slope, ca, thal]], columns=X.columns)
        prediction = model.predict(input_data)[0]
        if prediction==1:
            st.error("HIGH risk of heart disease")
        else:
            st.success("LOW risk of heart disease")
