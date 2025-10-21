import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

def heart():
    st.info("Approximate Heart Disease risk prediction.")

    url = 'https://drive.google.com/uc?id=155zmtpJU3_uxcl1BGRRScgrgvKcswHdt'
    df = pd.read_csv(url)

    scaler = StandardScaler()
    cols = ['age','trestbps','chol','thalach','oldpeak']
    df[cols] = scaler.fit_transform(df[cols])

    X = df.drop(['target'], axis=1)
    y = df['target']
    model = LogisticRegression()
    model.fit(X, y)

    form = st.form("heart_form")
    age = form.number_input("Age", min_value=1, max_value=120, value=30, key="age")
    sex = form.selectbox("Gender", ["Male","Female"], key="sex")
    cp = form.selectbox("Chest Pain Type", ["typical angina","atypical angina","non-anginal pain","asymptomatic"], key="cp")
    trestbps = form.number_input("Resting Blood Pressure", key="trestbps")
    chol = form.number_input("Serum Cholesterol", key="chol")
    thalach = form.number_input("Max Heart Rate", key="thalach")
    oldpeak = form.number_input("ST Depression", key="oldpeak")
    submitted = form.form_submit_button("Predict")

    if submitted:
        mapping = {"Male":1, "Female":0}
        cp_map = {"typical angina":1,"atypical angina":2,"non-anginal pain":3,"asymptomatic":4}
        input_df = pd.DataFrame([[
            age,
            mapping[sex],
            cp_map[cp],
            trestbps,
            chol,
            thalach,
            oldpeak
        ]], columns=['age','sex','cp','trestbps','chol','thalach','oldpeak'])
        pred = model.predict(input_df)[0]
        st.success("HIGH risk" if pred==1 else "LOW risk")
