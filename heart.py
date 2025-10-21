import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

def heart():
    st.info("Enter patient details for Heart Disease prediction.")

    url = 'https://drive.google.com/uc?id=155zmtpJU3_uxcl1BGRRScgrgvKcswHdt'
    df = pd.read_csv(url)
    scaler = StandardScaler()
    cols_to_scale = ['age','trestbps','chol','thalach','oldpeak']
    df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])

    form = st.form("HeartFormUI")
    age = form.number_input("Age", min_value=1, max_value=120, value=30)
    sex = form.radio("Gender", ['Male','Female'], key="sex_ui")
    cp = form.selectbox("Chest Pain Type", ['Typical','Atypical','Non-angina','Asymptomatic'], key="cp_ui")
    trestbps = form.number_input("Resting BP", value=120)
    chol = form.number_input("Cholesterol", value=200)
    fbs = form.radio("Fasting Blood Sugar >120 mg/dl", ['Yes','No'], key="fbs_ui")
    restecg = form.selectbox("Resting ECG", ['Normal','ST-T','LVH'], key="ecg_ui")
    thalach = form.number_input("Max Heart Rate", value=150)
    exang = form.radio("Exercise Induced Angina", ['Yes','No'], key="exang_ui")
    oldpeak = form.number_input("ST depression", value=1.0)
    slope = form.selectbox("Slope", ['Upsloping','Flat','Downsloping'], key="slope_ui")
    ca = form.selectbox("Major vessels colored", [0,1,2,3], key="ca_ui")
    thal = form.selectbox("Thalassemia", ['Normal','Fixed','Reversible'], key="thal_ui")
    submitted = form.form_submit_button("Predict")

    if submitted:
        mapping = {'Male':1,'Female':0,'Yes':1,'No':0,'Typical':1,'Atypical':2,'Non-angina':3,'Asymptomatic':4,
                   'Normal':0,'ST-T':1,'LVH':2,'Upsloping':1,'Flat':2,'Downsloping':3,'Normal':3,'Fixed':6,'Reversible':7}
        input_data = pd.DataFrame([[
            mapping[sex], mapping[cp], trestbps, chol, mapping[fbs], mapping[restecg],
            thalach, mapping[exang], oldpeak, mapping[slope], mapping[ca], mapping[thal]
        ]], columns=['sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal'])
        model = LogisticRegression()
        model.fit(df.drop('target',axis=1), df['target'])
        pred = model.predict(input_data)[0]
        st.balloons()
        st.success("HIGH risk!" if pred==1 else "LOW risk!")
