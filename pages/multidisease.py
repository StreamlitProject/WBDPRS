import streamlit as st
import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB

SYMPTOMS = [
    "itching", "skin_rash", "nodal_skin_eruptions", "continuous_sneezing",
    "shivering", "chills", "joint_pain", "stomach_pain", "acidity",
    "ulcers_on_tongue", "muscle_wasting", "vomiting", "burning_micturition",
    "spotting_ urination", "fatigue", "weight_gain", "anxiety",
    "cold_hands_and_feets", "mood_swings", "weight_loss", "restlessness",
    "lethargy", "patches_in_throat", "irregular_sugar_level", "cough",
    "high_fever", "sunken_eyes", "breathlessness", "sweating", "dehydration",
    "indigestion", "headache", "yellowish_skin", "dark_urine", "nausea",
    "loss_of_appetite", "pain_behind_the_eyes", "back_pain", "constipation",
    "abdominal_pain", "diarrhoea", "mild_fever", "yellow_urine",
    "yellowing_of_eyes", "acute_liver_failure", "fluid_overload",
    "swelling_of_stomach", "swelled_lymph_nodes", "malaise",
    "blurred_and_distorted_vision", "phlegm", "throat_irritation",
    "redness_of_eyes", "sinus_pressure", "runny_nose", "congestion",
    "chest_pain", "weakness_in_limbs", "fast_heart_rate",
    "pain_during_bowel_movements", "pain_in_anal_region", "bloody_stool",
    "irritation_in_anus", "neck_pain", "dizziness", "cramps", "bruising",
    "obesity", "swollen_legs", "swollen_blood_vessels", "puffy_face_and_eyes",
    "enlarged_thyroid", "brittle_nails", "swollen_extremeties",
    "excessive_hunger", "extra_marital_contacts", "drying_and_tingling_lips",
    "slurred_speech", "knee_pain", "hip_joint_pain", "muscle_weakness",
    "stiff_neck", "swelling_joints", "movement_stiffness",
    "spinning_movements", "loss_of_balance", "unsteadiness",
    "weakness_of_one_body_side", "loss_of_smell", "bladder_discomfort",
    "foul_smell_of urine", "continuous_feel_of_urine", "passage_of_gases",
    "internal_itching", "toxic_look_(typhos)", "depression", "irritability",
    "muscle_pain", "altered_sensorium", "red_spots_over_body", "belly_pain",
    "abnormal_menstruation", "dischromic _patches", "watering_from_eyes",
    "increased_appetite", "polyuria", "family_history", "mucoid_sputum",
    "rusty_sputum", "lack_of_concentration", "visual_disturbances",
    "receiving_blood_transfusion", "receiving_unsterile_injections", "coma",
    "stomach_bleeding", "distention_of_abdomen",
    "history_of_alcohol_consumption", "fluid_overload",
    "blood_in_sputum", "prominent_veins_on_calf", "palpitations",
    "painful_walking", "pus_filled_pimples", "blackheads", "scurring",
    "skin_peeling", "silver_like_dusting", "small_dents_in_nails",
    "inflammatory_nails", "blister", "red_sore_around_nose", "yellow_crust_ooze",
]

DISEASES = [
    "Fungal infection", "Allergy", "GERD", "Chronic cholestasis",
    "Drug Reaction", "Peptic ulcer disease", "AIDS", "Diabetes",
    "Gastroenteritis", "Bronchial Asthma", "Hypertension", "Migraine",
    "Cervical spondylosis", "Paralysis (brain hemorrhage)", "Jaundice",
    "Malaria", "Chicken pox", "Dengue", "Typhoid", "Hepatitis A",
    "Hepatitis B", "Hepatitis C", "Hepatitis D", "Hepatitis E",
    "Alcoholic hepatitis", "Tuberculosis", "Common Cold", "Pneumonia",
    "Dimorphic hemorrhoids (piles)", "Heart attack", "Varicose veins",
    "Hypothyroidism", "Hyperthyroidism", "Hypoglycemia", "Osteoarthritis",
    "Arthritis", "(vertigo) Paroxysmal Positional Vertigo", "Acne",
    "Urinary tract infection", "Psoriasis", "Impetigo",
]

DISEASE_MAP = {
    "Fungal infection": 0, "Allergy": 1, "GERD": 2,
    "Chronic cholestasis": 3, "Drug Reaction": 4,
    "Peptic ulcer diseae": 5, "AIDS": 6, "Diabetes ": 7,
    "Gastroenteritis": 8, "Bronchial Asthma": 9,
    "Hypertension ": 10, "Migraine": 11,
    "Cervical spondylosis": 12, "Paralysis (brain hemorrhage)": 13,
    "Jaundice": 14, "Malaria": 15, "Chicken pox": 16, "Dengue": 17,
    "Typhoid": 18, "hepatitis A": 19, "Hepatitis B": 20,
    "Hepatitis C": 21, "Hepatitis D": 22, "Hepatitis E": 23,
    "Alcoholic hepatitis": 24, "Tuberculosis": 25, "Common Cold": 26,
    "Pneumonia": 27, "Dimorphic hemmorhoids(piles)": 28,
    "Heart attack": 29, "Varicose veins": 30, "Hypothyroidism": 31,
    "Hyperthyroidism": 32, "Hypoglycemia": 33, "Osteoarthristis": 34,
    "Arthritis": 35, "(vertigo) Paroymsal  Positional Vertigo": 36,
    "Acne": 37, "Urinary tract infection": 38, "Psoriasis": 39,
    "Impetigo": 40,
}

SYMPTOM_FORMATTED = [s.replace("_", " ").replace("  ", " ").strip().title() for s in SYMPTOMS]


@st.cache_data
def load_training_data():
    traindf = pd.read_csv("Training.csv")
    testdf = pd.read_csv("Testing.csv")
    return traindf, testdf


@st.cache_resource
def train_model(traindf, testdf):
    traindf.replace({"prognosis": DISEASE_MAP}, inplace=True)
    testdf.replace({"prognosis": DISEASE_MAP}, inplace=True)

    X = traindf[SYMPTOMS]
    y = np.ravel(traindf[["prognosis"]])

    gnb = MultinomialNB()
    gnb.fit(X, y)
    return gnb


st.markdown("""
<div class="page-header">
    <h2>Multidisease Prediction</h2>
    <p>Select your symptoms to identify possible conditions</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="info-box">
    :bulb: **How it works:** Select the symptoms you are experiencing from the list below.
    The Naive Bayes classifier matches your symptom profile against 41 known diseases.
</div>
""", unsafe_allow_html=True)

with st.status("Loading model and training data...", expanded=False) as status:
    traindf, testdf = load_training_data()
    model = train_model(traindf, testdf)
    status.update(label="Model ready", state="complete")

st.badge("Naive Bayes", color="blue")

with st.form("Multidisease Prediction"):
    selected_symptoms = st.multiselect(
        "Select your symptoms (1-10)",
        options=SYMPTOM_FORMATTED,
        max_selections=10,
        placeholder="Start typing to search symptoms...",
    )

    submitted = st.form_submit_button("Check for Diseases", use_container_width=True)

if submitted:
    if len(selected_symptoms) == 0:
        st.warning("Please select at least one symptom.")
    else:
        with st.status("Analyzing symptoms...", expanded=True) as status:
            st.write(f"Processing {len(selected_symptoms)} symptom(s)...")
            feature_vector = [0] * len(SYMPTOMS)
            for sym in selected_symptoms:
                idx = SYMPTOM_FORMATTED.index(sym)
                feature_vector[idx] = 1

            st.write("Running classifier...")
            input_df = pd.DataFrame([feature_vector], columns=SYMPTOMS)
            prediction = model.predict(input_df)
            predicted_index = prediction[0]
            status.update(label="Prediction complete", state="complete", expanded=False)

        if predicted_index < len(DISEASES):
            predicted_disease = DISEASES[predicted_index]

            st.markdown(f"""
            <div class="result-card" style="border-left: 4px solid #ffaa00;">
                <div class="result-label">Predicted Condition</div>
                <div class="result-value" style="color: #ffaa00;">{predicted_disease}</div>
            </div>
            """, unsafe_allow_html=True)

            st.warning(
                "This is an approximate prediction based on symptom matching. "
                "Please consult a healthcare professional for proper diagnosis."
            )

            st.toast(f"Disease prediction: {predicted_disease}", icon="📋")

            with st.expander("View prediction details"):
                st.markdown(f"**Predicted disease:** {predicted_disease}")
                st.markdown(f"**Symptoms entered ({len(selected_symptoms)}):**")
                for sym in selected_symptoms:
                    st.markdown(f"- {sym}")

                st.divider()
                st.caption(
                    "Note: This model uses Naive Bayes classification on symptom data. "
                    "Results are indicative and should not replace professional medical advice."
                )
        else:
            st.info("No matching disease found for the given symptoms. Please consult a doctor.")
