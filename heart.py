import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

def heart():
    url = 'https://drive.google.com/uc?id=155zmtpJU3_uxcl1BGRRScgrgvKcswHdt'
    df = pd.read_csv(url)

    scaler = StandardScaler()
    for col in ['age','trestbps','chol','thalach','oldpeak']:
        df[col] = scaler.fit_transform(df[[col]])

    X = df.drop('target', axis=1)
    y = df['target']

    model = LogisticRegression()
    model.fit(X, y)

    form = st.form("heart_form")

    age = form.number_input("Age", min_value=1, max_value=120, value=30, key="heart_age")
    sex = form.radio("Gender", ['Male','Female'], key="heart_sex")
    cp = form.radio("Chest pain type", ['1 typical','2 atypical','3 non-angina','4 asymptomatic'], key="heart_cp")
    trestbps = form.number_input("Resting BP", key="heart_bp")
    chol = form.number_input("Cholesterol", key="heart_chol")
    fbs = form.radio("Fasting BS", ['Yes','No'], key="heart_fbs")
    restecg = form.radio("Rest ECG", ['Normal','Abnormal','Left hypertrophy'], key="heart_ecg")
    thalach = form.number_input("Max HR", key="heart_thalach")
    exang = form.radio("Exercise induced angina", ['Yes','No'], key="heart_exang")
    oldpeak = form.number_input("ST depression", key="heart_oldpeak")
    slope = form.radio("Slope", ['Up','Flat','Down'], key="heart_slope")
    ca = form.radio("Major vessels colored", [0,1,2,3], key="heart_ca")
    thal = form.radio("Defect type", ['Normal','Fixed','Reversible'], key="heart_thal")

    submitted = form.form_submit_button("Submit", key="heart_submit")

    if submitted:
        mapping = {
            'Male':1, 'Female':0,
            'Yes':1, 'No':0,
            '1 typical':1, '2 atypical':2, '3 non-angina':3, '4 asymptomatic':4,
            'Normal':0, 'Abnormal':1, 'Left hypertrophy':2,
            'Up':1, 'Flat':2, 'Down':3,
            'Fixed':6, 'Reversible':7
        }
        input_data = pd.DataFrame([[
            age, mapping[sex], mapping[cp], trestbps, chol, mapping[fbs], mapping[restecg],
            thalach, mapping[exang], oldpeak, mapping[slope], ca, mapping[thal]
        ]], columns=X.columns)
        pred = model.predict(input_data)[0]
        st.success("LOW risk" if pred==0 else "HIGH risk")
