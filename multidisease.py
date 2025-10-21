import streamlit as st
import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB

@st.cache_data
def load_data():
    train_df = pd.read_csv("Training.csv")
    train_df.columns = train_df.columns.str.strip()
    diseases = train_df['prognosis'].unique().tolist()
    disease_map = {d: i for i,d in enumerate(diseases)}
    train_df['prognosis'] = train_df['prognosis'].map(disease_map)
    return train_df, disease_map

@st.cache_data
def train_model(train_df, features):
    X = train_df[features].astype(int)
    y = train_df['prognosis'].values
    gnb = MultinomialNB()
    gnb.fit(X, y)
    return gnb

def multidisease():
    st.info("Select exactly 5 symptoms for prediction.")

    features = pd.read_csv("Training.csv").columns[:-1].tolist()
    train_df, disease_map = load_data()
    gnb = train_model(train_df, features)
    disease_list = list(disease_map.keys())

    symptoms = st.multiselect("Select Symptoms", options=features, max_selections=5, key="multi_ui")
    if st.button("Predict Disease"):
        if len(symptoms) != 5:
            st.warning("Select exactly 5 symptoms!")
        else:
            vec = [1 if f in symptoms else 0 for f in features]
            pred = gnb.predict([vec])[0]
            st.balloons()
            st.success(f"Predicted Disease: {disease_list[pred]}")
