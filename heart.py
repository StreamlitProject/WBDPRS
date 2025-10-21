# Loading libraries
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

def heart():
    # Load dataset from Google Drive
    url = 'https://drive.google.com/file/d/155zmtpJU3_uxcl1BGRRScgrgvKcswHdt/view?usp=sharing'
    url = 'https://drive.google.com/uc?id=' + url.split('/')[-2]
    df = pd.read_csv(url)

    # -------------------- Page Styling --------------------
    st.markdown("""
        <style>
        .css-12ttj6m {background-color: #6cdacf;}
        </style>
    """, unsafe_allow_html=True)

    # -------------------- Data Preprocessing --------------------
    columns_to_scale = ['age','trestbps','chol','thalach','oldpeak']
    scaler = StandardScaler()
    df[columns_to_scale] = scaler.fit_transform(df[columns_to_scale])

    X = df.drop(['target'], axis=1)
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=40)

    # Train logistic regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # -------------------- User Input Form --------------------
    form = st.form(key="Heart Disease Prediction")

    # Input fields
    age = form.number_input("Age in Years", min_value=1, max_value=120, value=30)
    
    sex_map = {'Male': 1, 'Female': 0}
    sex = sex_map[form.radio("Gender", ('Male', 'Female'))]

    cp_map = {'1= typical type 1':1, '2= typical type angina':2, '3= non-angina pain':3, '4= asymptomatic':4}
    cp = cp_map[form.radio("Chest pain type", tuple(cp_map.keys()))]

    thestbps = form.number_input("Resting blood pressure (mmHg)")
    chol = form.number_input("Serum cholesterol (mm/dL)")

    fbs_map = {'1 if ≥120 mg/dL':1, '0 if ≤120 mg/dL':0}
    fbs = fbs_map[form.radio("Fasting blood sugar", tuple(fbs_map.keys()))]

    restecg_map = {'0= normal':0, '1= ST-T wave abnormal':1, '2= left ventricular hypertrophy':2}
    restecg = restecg_map[form.radio("Resting electrographic results", tuple(restecg_map.keys()))]

    thalach = form.number_input("Maximum heart rate achieved")
    
    exang_map = {'0= no':0, '1= yes':1}
    exang = exang_map[form.radio("Exercise induced angina", tuple(exang_map.keys()))]

    oldpeak = form.number_input("ST depression induced by exercise relative to rest")

    slope_map = {'1= unsloping':1, '2= flat':2, '3= downsloping':3}
    slope = slope_map[form.radio("Slope of the peak exercise ST segment", tuple(slope_map.keys()))]

    ca_map = {'0':0, '1':1, '2':2, '3':3}
    ca = ca_map[form.radio("No. of major vessels colored by fluoroscopy", tuple(ca_map.keys()))]

    thal_map = {'3= normal':3, '6= fixed':6, '7= reversible defect':7}
    thal = thal_map[form.radio("Defect type", tuple(thal_map.keys()))]

    submitted = form.form_submit_button("Submit")

    # -------------------- Prediction --------------------
    if submitted:
        input_data = pd.DataFrame([[
            age, sex, cp, thestbps, chol, fbs, restecg, thalach,
            exang, oldpeak, slope, ca, thal
        ]], columns=X.columns)
        
        prediction = model.predict(input_data)[0]
        if prediction == 1:
            st.error("You are at HIGH risk of heart disease.")
        else:
            st.success("You are at LOW risk of heart disease.")
