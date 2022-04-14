#loading libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings('ignore')
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

def heart():
    url='https://drive.google.com/file/d/155zmtpJU3_uxcl1BGRRScgrgvKcswHdt/view?usp=sharing'
    url='https://drive.google.com/uc?id=' + url.split('/')[-2]
    df = pd.read_csv(url)

    style=f"""
    <style>
    .css-12ttj6m{{background-color: #6cdacf;}}
    </style>
    """
    st.markdown(style,unsafe_allow_html=True)
    #preparing data for the model
    #scaling of data
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import train_test_split
    StandardScaler = StandardScaler()
    columns_to_scale = ['age','trestbps','chol','thalach','oldpeak']
    df[columns_to_scale] = StandardScaler.fit_transform(df[columns_to_scale])
    X= df.drop(['target'], axis=1)
    y= df['target']
    X_train, X_test,y_train, y_test=train_test_split(X,y,test_size=0.3,random_state=40)
    
    #logistic regression
    from sklearn.linear_model import LogisticRegression
    lr=LogisticRegression()
    model1=lr.fit(X_train,y_train)
    #ptest=[-1.25367,1,	1,	1.049520,	0.014223,	1,	1,	0.933783,	0,	0.397182,	2,	0,	2]
    
    form = st.form(key="Heart Disease Prediction")
    #age {Age in Years-> continuous}
    age=form.number_input("Age in Years")
    
    #sex {Male or Female-> 1=male,0=female}
    sex_r=form.radio("Gender",('Male','Female'))
    if sex_r=="Male":
        sex=1
    elif sex_r=="Female":
        sex=0
    
    #cp {Chest pain type -> 1= typical type 1,2= typical type angina,non-angina pain,4= asymptomatic}
    cp_r=form.radio("Chest pain type",('1= typical type 1','2= typical type angina','3= non-angina pain','4= asymptotic'))
    if cp_r=='1= typical type 1':
        cp=1
    elif cp_r=='2= typical type angina':
        cp=2
    elif cp_r=='3= non-angina pain':
        cp=3
    elif cp_r=='4= asymptomatic':
        cp=4
    
    #thestbps {Resting blood pressure-> Continuous value in mmHg}
    thestbps=form.number_input("Resting blood pressure (in mmHg)")
    
    #chol {Serum cholesterol->Continuous value in mm/dL}
    chol=form.number_input("Serum cholestrol (in mm/dL)")
    
    #fbs {Fasting blood sugar->1≥120 mg/dL, 0≤120 mg/dL }
    fbs_r=form.radio("Fasting blood sugar",('1 if ≥120 mg/dL','0 if ≤120 mg/dL'))
    if fbs_r=='1 if ≥120 mg/dL':
        fbs=1
    elif fbs_r=='0 if ≤120 mg/dL':
        fbs=0
    

    #restecg {Resting electrographic results->0= normal,1= having ST-T wave abnormal,2= left ventricular hypertrophy}
    restecg_r=form.radio("Resting electrographic results",('0= normal','1= having ST-T wave abnormal','2= left ventricular hypertrophy'))
    if restecg_r=='0= normal':
        restecg=0
    elif restecg_r=='1= having ST-T wave abnormal':
        restecg=1
    elif restecg_r=='2= left ventricular hypertrophy':
        restecg=2
    
    #thalach {Maximum heart rate achieved-> Continuous value}
    thalach=form.number_input("Maximum heart rate achieved")
    
    #exang {Exercise induced angina-> 0= no,1= yes}
    exang_r=form.radio("Exercise induced angina",("0= no","1= yes"))
    if exang_r=="0= no":
        exang=0
    elif exang_r=="1= yes":
        exang=1
    
    #old peak {ST depression induced by exercise relative to rest -> Continuous value}
    old_peak=form.number_input("ST depression induced by exercise relative to rest")
    

    #slope {Slope of the peak exercise ST segment ->1= unsloping,2= flat,3= downsloping}
    slope_r=form.radio("Slope of the peak exercise ST segment",("1= unsloping","2= flat","3= downsloping"))
    if slope_r=="1= unsloping":
        slope=1
    elif slope_r=="2= flat":
        slope=2
    elif slope_r=="3= downsloping":
        slope=3
    
    #ca {Number of major vessels colored by fluoroscopy->0–3 value}
    ca_r=form.radio("No. of major vessels colored by fluoroscopy",("0","1","2","3"))
    if ca_r=="0":
        ca=0
    elif ca_r=="1":
        ca=1
    elif ca_r=="2":
        ca=2
    elif ca_r=="3":
        ca=3
    
    #thal {Defect type-> 3= normal,6= fixed,7= reversible defect}
    thal_r=form.radio("Defect type",("3= normal","6= fixed","7= reversible defect"))
    if thal_r=="3= normal":
        thal=3
    elif thal_r=="6= fixed":
        thal=6
    elif thal_r=="7= reversible defect":
        thal=7

    Submitted=form.form_submit_button("Submit")


    ptest=[]
    ptest.append(age)
    ptest.append(sex)
    ptest.append(cp)
    ptest.append(thestbps)
    ptest.append(chol)
    ptest.append(fbs)
    ptest.append(restecg)
    ptest.append(thalach)
    ptest.append(exang)
    ptest.append(old_peak)
    ptest.append(slope)
    ptest.append(ca)
    ptest.append(thal)
    if Submitted:
        #ptest=[age,sex,cp,thestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        columns=['age','sex','cp','thestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']
        take=pd.DataFrame(ptest,columns)
        take=take.T
        k=model1.predict(take)
        if(k==1):
            st.write("You are at high risk to heart disease")
        elif(k==0):
            st.write("You are at low risk to heart disease")