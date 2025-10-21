import streamlit as st
import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB

@st.cache_data
def load_data():
    train_df = pd.read_csv("Training.csv")
    test_df = pd.read_csv("Testing.csv")
    disease_list = list(set(train_df['prognosis'].str.strip()))
    disease_map = {d:i for i,d in enumerate(disease_list)}
    train_df['prognosis'] = train_df['prognosis'].map(disease_map)
    test_df['prognosis'] = test_df['prognosis'].map(disease_map)
    return train_df, test_df, disease_map

@st.cache_data
def train_model(train_df, features):
    X = train_df[features].astype(int)
    y = train_df['prognosis'].values
    model = MultinomialNB()
    model.fit(X,y)
    return model

def multidisease():
    st.markdown("## Predict Disease from Symptoms")
    st.info("Approximate predictions using an AI model. Select exactly 5 symptoms.")

    features = pd.read_csv("Training.csv").columns[:-1].tolist()
    traindf, testdf, disease_map = load_data()
    model = train_model(traindf, features)
    disease_list = list(disease_map.keys())

    symptoms = st.multiselect("Select 5 symptoms:", options=features)
    if st.button("Predict"):
        if len(symptoms)!=5:
            st.warning("Please select exactly 5 symptoms.")
        else:
            input_vector = [1 if s in symptoms else 0 for s in features]
            pred_idx = model.predict([input_vector])[0]
            st.success(f"Predicted Disease: {disease_list[pred_idx]}")
