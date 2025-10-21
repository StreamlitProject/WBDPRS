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
    disease_map = {disease:i for i,disease in enumerate(disease_list)}
    train_df['prognosis'] = train_df['prognosis'].map(disease_map)
    train_df.dropna(subset=['prognosis'], inplace=True)
    train_df['prognosis'] = train_df['prognosis'].astype(int)
    return train_df, disease_map

@st.cache_data
def train_model(train_df, features):
    X = train_df[features].astype(int)
    y = train_df['prognosis'].values
    gnb = MultinomialNB()
    gnb.fit(X, y)
    return gnb

def multidisease():
    st.markdown("## Have A Quick Overlook :eyes:")
    st.info("Select exactly 5 symptoms to predict your disease.")

    features = ['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering',
                'chills','joint_pain','stomach_pain','acidity','ulcers_on_tongue','muscle_wasting',
                'vomiting','burning_micturition','spotting_ urination','fatigue','weight_gain']

    train_df, disease_map = load_data()
    model = train_model(train_df, features)
    disease_list = list(disease_map.keys())

    psymptoms = st.multiselect("Select exactly 5 Symptoms", features)
    if st.button("Submit"):
        if len(psymptoms) != 5:
            st.warning("Please select exactly 5 symptoms.")
        else:
            input_vector = [1 if s in psymptoms else 0 for s in features]
            pred_index = model.predict([input_vector])[0]
            st.success(f"Predicted Disease: {disease_list[pred_index]}")
