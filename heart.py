import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

def heart():
    st.header("Heart Disease Risk Prediction")
    st.info("Approximate risk prediction (under development).")

    url = 'https://drive.google.com/uc?id=155zmtpJU3_uxcl1BGRRScgrgvKcswHdt'
    df = pd.read_csv(url)
    cols = ['age','trestbps','chol','thalach','oldpeak']
    df[cols] = StandardScaler().fit_transform(df[cols])

    X = df.drop(['target'], axis=1)
    y = df['target']
    model = LogisticRegression()
    model.fit(X,y)

    with st.form("heart_form"):
        age = st.number_input("Age", min_value=1,max_value=120,value=30,key="age")
        sex = st.selectbox("Gender", ["Male","Female"], key="sex")
        cp = st.selectbox("Chest Pain Type", ["typical angina","atypical angina","non-anginal pain","asymptomatic"], key="cp")
        trestbps = st.number_input("Resting BP", key="trestbps")
        chol = st.number_input("Cholesterol", key="chol")
        thalach = st.number_input("Max Heart Rate", key="thalach")
        oldpeak = st.number_input("ST Depression", key="oldpeak")
        submit = st.form_submit_button("Predict")

    if submit:
        sex_map = {"Male":1,"Female":0}
        cp_map = {"typical angina":1,"atypical angina":2,"non-anginal pain":3,"asymptomatic":4}
        input_df = pd.DataFrame([[age, sex_map[sex], cp_map[cp], trestbps, chol, thalach, oldpeak]],
                                columns=['age','sex','cp','trestbps','chol','thalach','oldpeak'])
        pred = model.predict(input_df)[0]
        st.success("HIGH risk" if pred==1 else "LOW risk")
