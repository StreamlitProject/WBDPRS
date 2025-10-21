import streamlit as st
import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB

@st.cache_data
def load_data():
    train_df = pd.read_csv("Training.csv")
    test_df = pd.read_csv("Testing.csv")

    # Remove leading/trailing spaces in column names
    train_df.columns = train_df.columns.str.strip()
    test_df.columns = test_df.columns.str.strip()

    # Map diseases to numbers
    disease_list = [
        'Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction', 
        'Peptic ulcer diseae', 'AIDS', 'Diabetes', 'Gastroenteritis', 'Bronchial Asthma', 
        'Hypertension', 'Migraine', 'Cervical spondylosis', 'Paralysis (brain hemorrhage)', 
        'Jaundice', 'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'hepatitis A', 'Hepatitis B', 
        'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Alcoholic hepatitis', 'Tuberculosis', 
        'Common Cold', 'Pneumonia', 'Dimorphic hemmorhoids(piles)', 'Heartattack', 'Varicoseveins', 
        'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia', 'Osteoarthristis', 'Arthritis', 
        '(vertigo) Paroymsal  Positional Vertigo', 'Acne', 'Urinary tract infection', 'Psoriasis', 'Impetigo'
    ]
    disease_map = {disease: i for i, disease in enumerate(disease_list)}

    # Replace disease names with numeric codes
    train_df['prognosis'] = train_df['prognosis'].map(disease_map)
    test_df['prognosis'] = test_df['prognosis'].map(disease_map)

    # Drop rows with missing values after mapping
    train_df.dropna(subset=['prognosis'], inplace=True)
    test_df.dropna(subset=['prognosis'], inplace=True)

    # Ensure integer type
    train_df['prognosis'] = train_df['prognosis'].astype(int)
    test_df['prognosis'] = test_df['prognosis'].astype(int)

    return train_df, test_df, disease_map

@st.cache_data
def train_model(train_df, features):
    X = train_df[features].astype(int)
    y = train_df['prognosis'].values  # 1D numeric array
    gnb = MultinomialNB()
    gnb.fit(X, y)
    return gnb

def multidisease():
    st.markdown("## Have A Quick Overlook :eyes:")
    st.text("Step I: Scroll down and use the template to predict your disease based on symptoms.")
    st.text("Step II: Select exactly five symptoms from the dropdowns.")
    st.text("Step III: Click Submit to see the prediction.\n")
    st.markdown("That's cool :sunglasses:")
    st.info("Note: You will see the approximate disease matching your symptoms.")

    # Feature columns
    l1 = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering',
          'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting',
          'vomiting', 'burning_micturition', 'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety',
          'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy',
          'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes',
          'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish_skin',
          'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation',
          'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes',
          'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes',
          'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes',
          'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
          'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
          'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs',
          'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails',
          'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips',
          'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck',
          'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance',
          'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort',
          'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching',
          'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium',
          'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic _patches',
          'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum',
          'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion',
          'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen',
          'history_of_alcohol_consumption', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations',
          'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
          'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister',
          'red_sore_around_nose', 'yellow_crust_ooze']

    traindf, testdf, disease_map = load_data()
    gnb = train_model(traindf, l1)
    disease_list = list(disease_map.keys())

    form = st.form(key="MDP")
    psymptoms = form.multiselect("Select exactly 5 Symptoms", options=l1)
    submitted = form.form_submit_button("Submit")

    if submitted:
        if len(psymptoms) != 5:
            st.warning("Please select exactly 5 symptoms.")
        else:
            input_vector = [1 if symptom in psymptoms else 0 for symptom in l1]
            predicted_index = gnb.predict([input_vector])[0]
            st.success(f"Predicted Disease: {disease_list[predicted_index]}")
