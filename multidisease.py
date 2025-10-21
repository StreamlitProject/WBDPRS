import streamlit as st
import pandas as pd
from sklearn.naive_bayes import MultinomialNB

@st.cache_data
def load_data():
    train = pd.read_csv("Training.csv")
    test = pd.read_csv("Testing.csv")
    return train, test

@st.cache_data
def train_model(train, features):
    X = train[features]
    y = train['prognosis']
    model = MultinomialNB()
    model.fit(X, y)
    return model

def multidisease():
    st.header("Multidisease Prediction")
    st.info("Prediction based on symptoms")

    train, test = load_data()
    features = train.columns[:-1].tolist()
    model = train_model(train, features)

    symptoms = st.multiselect("Select up to 5 symptoms", options=features, max_selections=5, key="multi_symptoms")

    if st.button("Predict", key="multi_predict"):
        if not symptoms:
            st.warning("Select at least 1 symptom")
        else:
            vector = [1 if f in symptoms else 0 for f in features]
            pred = model.predict([vector])[0]
            st.success(f"Predicted Disease Code: {pred}")
