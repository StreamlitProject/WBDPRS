import streamlit as st
import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB

@st.cache_data
def load_data():
    train_df = pd.read_csv("Training.csv")
    test_df = pd.read_csv("Testing.csv")
    train_df.columns = train_df.columns.str.strip()
    test_df.columns = test_df.columns.str.strip()

    disease_list = ['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
                    'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma',
                    'Hypertension','Migraine','Cervical spondylosis','Paralysis (brain hemorrhage)',
                    'Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A','Hepatitis B',
                    'Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
                    'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)','Heartattack','Varicoseveins',
                    'Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis','Arthritis',
                    '(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis','Impetigo']
    disease_map = {d:i for i,d in enumerate(disease_list)}

    train_df['prognosis'] = train_df['prognosis'].map(disease_map)
    test_df['prognosis'] = test_df['prognosis'].map(disease_map)
    train_df.dropna(subset=['prognosis'], inplace=True)
    test_df.dropna(subset=['prognosis'], inplace=True)
    train_df['prognosis'] = train_df['prognosis'].astype(int)
    test_df['prognosis'] = test_df['prognosis'].astype(int)

    return train_df, test_df, disease_map

@st.cache_data
def train_model(train_df, features):
    X = train_df[features].astype(int)
    y = train_df['prognosis'].values
    gnb = MultinomialNB()
    gnb.fit(X, y)
    return gnb

def multidisease():
    st.info("Select 5 symptoms to predict possible disease.")

    features = ['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering']
    train_df, test_df, disease_map = load_data()
    gnb = train_model(train_df, features)

    form = st.form("multidisease_form")
    symptoms = form.multiselect("Select exactly 5 Symptoms", options=features, key="multi_symptoms")
    submitted = form.form_submit_button("Submit", key="multi_submit")

    if submitted:
        if len(symptoms) != 5:
            st.warning("Select exactly 5 symptoms!")
        else:
            input_vec = [1 if f in symptoms else 0 for f in features]
            pred_idx = gnb.predict([input_vec])[0]
            st.success(f"Predicted Disease: {list(disease_map.keys())[pred_idx]}")
