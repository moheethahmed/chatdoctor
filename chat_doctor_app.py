import streamlit as st
import pandas as pd
import pickle
from gtts import gTTS
import base64

# Load model and data
model = pickle.load(open('disease_model.pkl', 'rb'))
data = pd.read_csv('disease_dataset.csv')
symptoms = data.columns[:-1].tolist()

# Disease remedies
disease_remedies = {
    'Flu': 'Stay hydrated, rest, and use over-the-counter medications.',
    'Cold': 'Rest, drink fluids, and use nasal sprays.',
    'Migraine': 'Use prescribed medications, rest in a dark room, and avoid triggers.',
    'Allergy': 'Avoid allergens and take antihistamines.',
    'Asthma': 'Use inhalers, avoid allergens, and stay indoors if needed.',
    'COVID-19': 'Isolate, monitor oxygen, and consult a doctor.',
    'Malaria': 'Take antimalarial medications and consult a doctor immediately.',
    'Dengue': 'Drink plenty of fluids and consult a doctor.',
    'Typhoid': 'Antibiotics and proper hydration are essential.',
    'Jaundice': 'Rest, hydration, and avoid fatty foods.'
}

# Streamlit UI config
st.set_page_config(page_title="ChatDoctor AI", layout="centered")

# Custom styling
st.markdown(
    """
    <style>
    body, .stApp {
        background-color: #fefaf1;
        color: black;
    }
    h1, h2, h3, h4, h5, h6, p {
        color: black !important;
    }
    .stMultiSelect>div>div>div {
        background-color: white !important;
        color: black !important;
        border: 2px solid red;
    }
    .stMultiSelect span {
        color: black !important;
    }
    .stButton>button {
        background-color: white;
        color: black;
        border: 2px solid red;
        padding: 6px 20px;
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown("<h1>🩺 ChatDoctor AI</h1>", unsafe_allow_html=True)
st.write("Enter your symptoms below, and we'll suggest a possible condition with remedies.")

# Input
selected_symptoms = st.multiselect("Choose your symptoms:", symptoms)

if st.button("Diagnose"):
    input_data = [1 if symptom in selected_symptoms else 0 for symptom in symptoms]
    prediction = model.predict([input_data])[0]
    remedy = disease_remedies.get(prediction, "Consult a professional doctor.")

    st.success(f"🔍 You may have: **{prediction}**")
    st.info(f"💡 Remedy: 🧑‍⚕️ {remedy}")
    st.warning("📌 DISCLAIMER: ALWAYS CONSULT A PROFESSIONAL DOCTOR FOR REAL DIAGNOSIS.")

    # Text-to-speech
    message = f"Based on your symptoms, you may have {prediction}. Remedy is: {remedy}."
    tts = gTTS(message)
    tts.save("voice.mp3")

    with open("voice.mp3", "rb") as audio_file:
        audio_bytes = audio_file.read()
        b64 = base64.b64encode(audio_bytes).decode()

        st.markdown(
            f"""
            <audio autoplay>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """,
            unsafe_allow_html=True
        )
