import streamlit as st
import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB

@st.cache_data
def load_data():
    df_train = pd.read_csv("Training.csv")
    df_test = pd.read_csv("Testing.csv")
    df_train.columns = df_train.columns.str.strip()
    df_test.columns = df_test.columns.str.strip()

    diseases = sorted(df_train['prognosis'].unique())
    disease_map = {d:i for i,d in enumerate(diseases)}
    df_train['prognosis'] = df_train['prognosis'].map(disease_map)
    return df_train, disease_map

@st.cache_data
def train_model(df, features):
    X = df[features].astype(int)
    y = df['prognosis'].values
    model = MultinomialNB()
    model.fit(X, y)
    return model

def multidisease():
    st.markdown("## Multi-Disease Predictor :stethoscope:")
    st.info("Select exactly 5 symptoms to predict probable disease.")

    features = ['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain','stomach_pain']
    df_train, disease_map = load_data()
    model = train_model(df_train, features)
    disease_list = list(disease_map.keys())

    form = st.form(key="MD")
    symptoms = form.multiselect("Select 5 Symptoms", options=features)
    submit = form.form_submit_button("Submit")

    if submit:
        if len(symptoms)!=5:
            st.warning("Select exactly 5 symptoms")
        else:
            vector = [1 if f in symptoms else 0 for f in features]
            pred = model.predict([vector])[0]
            st.success(f"Predicted Disease: {disease_list[pred]}")
