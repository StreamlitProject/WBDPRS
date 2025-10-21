import streamlit as st
import pandas as pd
from sklearn.naive_bayes import MultinomialNB

@st.cache_data
def load_data():
    train_df = pd.read_csv("Training.csv")
    test_df = pd.read_csv("Testing.csv")
    return train_df, test_df

@st.cache_data
def train_model(train_df, features):
    X = train_df[features]
    y = train_df['prognosis']
    model = MultinomialNB()
    model.fit(X, y)
    return model

def multidisease():
    st.info("Approximate disease prediction based on symptoms.")

    train_df, test_df = load_data()
    features = train_df.columns[:-1].tolist()
    model = train_model(train_df, features)

    symptoms = st.multiselect(
        "Select up to 5 symptoms",
        options=features,
        max_selections=5,
        key="multi_symptoms"
    )

    if st.button("Predict Disease", key="multi_predict"):
        if len(symptoms) == 0:
            st.warning("Select at least 1 symptom")
        else:
            input_vector = [1 if f in symptoms else 0 for f in features]
            pred_idx = model.predict([input_vector])[0]
            st.success(f"Predicted Disease Code: {pred_idx}")
