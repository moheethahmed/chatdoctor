import streamlit as st
import pandas as pd
import pickle
from gtts import gTTS
import tempfile

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

# gTTS speech function
def speak(text):
    tts = gTTS(text=text, lang='en')
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        st.audio(fp.name, format='audio/mp3')

# Streamlit UI Styling
st.set_page_config(page_title="ChatDoctor AI", layout="centered")
st.markdown(
    """
    <style>
        .stApp {
            background-color: #fdfcf7;
        }
        h1, .st-bb {
            color: red;
        }
        .stMarkdown, label, div {
            color: black;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🩺 ChatDoctor AI")
st.markdown("Enter your symptoms below, and we'll suggest a possible condition with remedies.")

# User Input
selected_symptoms = st.multiselect("Choose your symptoms:", options=symptoms)

# Prediction
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

        speak_text = f"Based on your symptoms, you may have {disease}. Suggested remedy: {remedy}"
        speak(speak_text)
