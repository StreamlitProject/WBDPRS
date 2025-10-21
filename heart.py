import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

def heart():
    st.markdown("## Heart Disease Prediction")
    st.info("Approximate prediction using logistic regression model.")

    url = 'https://drive.google.com/uc?id=155zmtpJU3_uxcl1BGRRScgrgvKcswHdt'
    df = pd.read_csv(url)

    scaler = StandardScaler()
    for col in ['age','trestbps','chol','thalach','oldpeak']:
        df[col] = scaler.fit_transform(df[[col]])

    X = df.drop('target',axis=1)
    y = df['target']
    model = LogisticRegression()
    model.fit(X,y)

    # User input form
    age = st.number_input("Age", 1,120,30)
    sex = st.radio("Gender", ["Male","Female"], horizontal=True)
    cp = st.selectbox("Chest pain type", ['typical angina','atypical angina','non-angina','asymptomatic'])
    thestbps = st.number_input("Resting BP")
    chol = st.number_input("Cholesterol")
    fbs = st.radio("Fasting blood sugar", ["<120","≥120"], horizontal=True)
    restecg = st.selectbox("Resting ECG", ['Normal','ST-T abnormal','LV hypertrophy'])
    thalach = st.number_input("Max heart rate")
    exang = st.radio("Exercise induced angina", ["No","Yes"], horizontal=True)
    oldpeak = st.number_input("ST depression")
    slope = st.selectbox("Slope of ST segment", ['Up','Flat','Down'])
    ca = st.selectbox("Major vessels colored", [0,1,2,3])
    thal = st.selectbox("Defect type", ['Normal','Fixed','Reversible'])

    if st.button("Predict"):
        input_df = pd.DataFrame([[age,1 if sex=='Male' else 0,
                                  ['typical angina','atypical angina','non-angina','asymptomatic'].index(cp)+1,
                                  thestbps, chol, 1 if fbs=='≥120' else 0,
                                  ['Normal','ST-T abnormal','LV hypertrophy'].index(restecg),
                                  thalach,1 if exang=='Yes' else 0, oldpeak,
                                  ['Up','Flat','Down'].index(slope)+1, ca,
                                  ['Normal','Fixed','Reversible'].index(thal)+3]],
                                columns=X.columns)
        pred = model.predict(input_df)[0]
        if pred==1: st.error("HIGH risk of heart disease")
        else: st.success("LOW risk of heart disease")
