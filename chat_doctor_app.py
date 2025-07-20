import streamlit as st
import pandas as pd
import pickle
import pyttsx3

# Load model and encoder
model = pickle.load(open("chatdoctor_model.pkl", "rb"))
le = pickle.load(open("label_encoder.pkl", "rb"))

# Load symptoms and dataset
df = pd.read_csv("chatdoctor_expanded_dataset.csv")
symptoms = df.columns[:-1].tolist()

# Remedies
remedies = {
    "Common Cold": "🛌 Rest, stay hydrated, and use saline nasal spray.",
    "Flu": "💧 Drink fluids and rest. Antiviral meds may help.",
    "COVID-19": "😷 Isolate, monitor oxygen, and consult a doctor.",
    "Migraine": "🕶️ Rest in a quiet dark room and avoid triggers.",
    "Food Poisoning": "🥤 Stay hydrated and avoid solid food for some time.",
    "Malaria": "💊 Use antimalarial meds and rest well.",
    "Dengue": "🩸 Stay hydrated and monitor platelet count.",
    "Typhoid": "💧 Drink clean water and follow antibiotics.",
    "Sinusitis": "🌡️ Use steam inhalation and nasal decongestants.",
    "Bronchitis": "🌬️ Use humidifier, drink warm fluids, and rest.",
    "Tuberculosis": "💊 Complete TB treatment and maintain good nutrition.",
    "Asthma": "💨 Use inhalers, avoid allergens, and stay indoors if needed.",
    "Pneumonia": "💊 Take prescribed antibiotics and stay warm and hydrated.",
    "Diabetes": "🩸 Monitor sugar, eat balanced meals, and stay active.",
    "Hypertension": "💓 Reduce salt, manage stress, and take meds regularly.",
    "Anemia": "🥩 Eat iron-rich foods and take supplements.",
    "Allergy": "💊 Use antihistamines and avoid triggers.",
    "Depression": "🧠 Talk therapy, regular exercise, and support are key.",
    "Anxiety": "🧘 Practice breathing, reduce caffeine, and talk to someone.",
    "Chickenpox": "❄️ Calamine lotion for itching and avoid close contact."
}

# Text-to-speech setup
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()

# Streamlit App UI
st.set_page_config(page_title="ChatDoctor AI", layout="centered")
st.title("🩺 ChatDoctor AI")
st.markdown("Enter your symptoms below, and we'll suggest a possible condition with remedies.")

# User input: symptom selection
selected_symptoms = st.multiselect("Choose your symptoms:", options=symptoms)

if st.button("Diagnose"):
    if not selected_symptoms:
        st.warning("Please select at least one symptom.")
    else:
        input_vector = [1 if s in selected_symptoms else 0 for s in symptoms]
        predicted = model.predict([input_vector])[0]
        disease = le.inverse_transform([predicted])[0]
        remedy = remedies.get(disease, "❗ Please consult a healthcare provider for treatment advice.")

        st.success(f"🔍 You may have: **{disease}**")
        st.info(f"💡 Remedy: {remedy}")
        st.error("📌 DISCLAIMER: ALWAYS CONSULT A PROFESSIONAL DOCTOR FOR REAL DIAGNOSIS.")

        # Speak the result
        speak_text = f"Based on your symptoms, you may have {disease}. Suggested remedy: {remedy}"
        speak(speak_text)
