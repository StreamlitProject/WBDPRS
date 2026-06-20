import streamlit as st
import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB

SYMPTOM_CATEGORIES = {
    "General": [
        "fatigue", "fever", "malaise", "lethargy", "restlessness",
        "weight_gain", "weight_loss", "anxiety", "depression",
    ],
    "Skin": [
        "itching", "skin_rash", "nodal_skin_eruptions", "pus_filled_pimples",
        "blackheads", "scurring", "skin_peeling", "silver_like_dusting",
        "blister", "red_sore_around_nose", "yellow_crust_ooze",
        "dischromic _patches", "red_spots_over_body",
    ],
    "Respiratory": [
        "continuous_sneezing", "cough", "breathlessness", "phlegm",
        "throat_irritation", "patches_in_throat", "runny_nose",
        "congestion", "sinus_pressure", "mucoid_sputum", "rusty_sputum",
        "blood_in_sputum",
    ],
    "Digestive": [
        "stomach_pain", "acidity", "ulcers_on_tongue", "vomiting",
        "indigestion", "nausea", "loss_of_appetite", "constipation",
        "diarrhoea", "abdominal_pain", "pain_behind_the_eyes",
        "yellowish_skin", "dark_urine", "yellow_urine", "yellowing_of_eyes",
    ],
    "Pain & Joints": [
        "joint_pain", "back_pain", "neck_pain", "knee_pain",
        "hip_joint_pain", "muscle_pain", "muscle_weakness",
        "muscle_wasting", "cramps", "stiff_neck", "swelling_joints",
        "movement_stiffness", "painful_walking",
    ],
    "Cardiovascular": [
        "chest_pain", "fast_heart_rate", "palpitations",
        "swollen_legs", "swollen_blood_vessels", "prominent_veins_on_calf",
    ],
    "Neurological": [
        "headache", "dizziness", "spinning_movements", "loss_of_balance",
        "unsteadiness", "weakness_of_one_body_side", "slurred_speech",
        "loss_of_smell", "loss_of_smell", "altered_sensorium",
        "lack_of_concentration", "visual_disturbances",
        "blurred_and_distorted_vision",
    ],
    "Urinary": [
        "burning_micturition", "spotting_ urination", "dark_urine",
        "bladder_discomfort", "foul_smell_of urine",
        "continuous_feel_of_urine", "polyuria",
    ],
    "Other": [
        "shivering", "chills", "sweating", "dehydration", "sunken_eyes",
        "mood_swings", "cold_hands_and_feets", "puffy_face_and_eyes",
        "enlarged_thyroid", "brittle_nails", "swollen_extremeties",
        "excessive_hunger", "extra_marital_contacts",
        "drying_and_tingling_lips", "swelled_lymph_nodes",
        "passage_of_gases", "internal_itching", "toxic_look_(typhos)",
        "irritability", "redness_of_eyes", "belly_pain",
        "abnormal_menstruation", "watering_from_eyes", "increased_appetite",
        "family_history", "receiving_blood_transfusion",
        "receiving_unsterile_injections", "coma", "stomach_bleeding",
        "distention_of_abdomen", "history_of_alcohol_consumption",
        "obesity", "irritation_in_anus", "pain_in_anal_region",
        "bloody_stool", "weakness_in_limbs",
    ],
}

ALL_SYMPTOMS = []
SYMPTOM_TO_FORMATTED = {}
for cat, syms in SYMPTOM_CATEGORIES.items():
    for s in syms:
        if s not in SYMPTOM_TO_FORMATTED:
            ALL_SYMPTOMS.append(s)
            formatted = s.replace("_", " ").replace("  ", " ").strip().title()
            SYMPTOM_TO_FORMATTED[s] = formatted

FORMATTED_TO_RAW = {v: k for k, v in SYMPTOM_TO_FORMATTED.items()}

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


@st.cache_data
def load_training_data():
    traindf = pd.read_csv("Training.csv")
    testdf = pd.read_csv("Testing.csv")
    return traindf.copy(), testdf.copy()


@st.cache_resource
def train_model(_traindf, _testdf):
    traindf = _traindf.copy()
    testdf = _testdf.copy()
    traindf.replace({"prognosis": DISEASE_MAP}, inplace=True)
    testdf.replace({"prognosis": DISEASE_MAP}, inplace=True)

    X = traindf[ALL_SYMPTOMS]
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

with st.popover("How it works"):
    st.markdown("""
    Select the symptoms you are experiencing. The Naive Bayes classifier
    matches your symptom profile against 41 known diseases.

    **Model:** Multinomial Naive Bayes
    **Features:** Symptom binary indicators
    **Classes:** 41 diseases
    """)

try:
    with st.spinner("Loading model..."):
        traindf, testdf = load_training_data()
        model = train_model(traindf, testdf)
    st.badge("Naive Bayes", color="blue")
except Exception as e:
    st.error(f"Failed to load multidisease model: {e}")
    st.stop()

selected_symptoms = []

st.markdown("**Select your symptoms**")
category_tabs = st.tabs(list(SYMPTOM_CATEGORIES.keys()))

for tab, (cat_name, cat_symptoms) in zip(category_tabs, SYMPTOM_CATEGORIES.items()):
    with tab:
        formatted_options = [SYMPTOM_TO_FORMATTED[s] for s in cat_symptoms if s in SYMPTOM_TO_FORMATTED]
        chosen = st.multiselect(
            cat_name,
            options=formatted_options,
            key=f"cat_{cat_name}",
            label_visibility="collapsed",
            placeholder=f"Search {cat_name.lower()} symptoms...",
        )
        for c in chosen:
            selected_symptoms.append(c)

if selected_symptoms:
    st.info(f"**{len(selected_symptoms)}** symptom{'s' if len(selected_symptoms) != 1 else ''} selected")

if st.button("Check for Diseases", width="stretch", type="primary"):
    if len(selected_symptoms) == 0:
        st.warning("Please select at least one symptom.")
    else:
        with st.spinner("Analyzing symptoms..."):
            feature_vector = [0] * len(ALL_SYMPTOMS)
            for sym in selected_symptoms:
                raw = FORMATTED_TO_RAW.get(sym)
                if raw and raw in ALL_SYMPTOMS:
                    idx = ALL_SYMPTOMS.index(raw)
                    feature_vector[idx] = 1

            input_df = pd.DataFrame([feature_vector], columns=ALL_SYMPTOMS)
            prediction = model.predict(input_df)
            predicted_index = prediction[0]

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

            if "history" not in st.session_state:
                st.session_state.history = []
            st.session_state.history.append({
                "Module": "Multidisease",
                "Result": predicted_disease,
                "Confidence": "N/A",
            })

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

            st.markdown("---")
            st.markdown("**Was this prediction helpful?**")
            feedback = st.feedback("faces")
            if feedback is not None:
                st.session_state.history[-1]["Rating"] = f"{feedback}/2"
                st.toast("Thanks for your feedback!", icon="⭐")
        else:
            st.info("No matching disease found for the given symptoms. Please consult a doctor.")
