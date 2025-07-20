# ChatDoctor AI

ChatDoctor AI is a machine learning-powered web application that predicts possible diseases based on user-selected symptoms and suggests simple home remedies. It features a clean hospital-themed UI and includes a built-in voice assistant that reads out the diagnosis.

---

## Features

- Select symptoms from a predefined list  
- Predicts the most likely condition using a trained ML model  
- Displays suggested remedies for the predicted condition  
- Speaks out the diagnosis using Google Text-to-Speech  
- Clean, hospital-style user interface with themed styling

---

## How It Works

1. **User Input**: The user selects symptoms from a list in the UI.  
2. **ML Prediction**: The app converts the symptoms into a one-hot encoded input vector and feeds it to a trained machine learning model.  
3. **Label Decoding**: The model predicts a disease, which is decoded using a label encoder.  
4. **Remedy Retrieval**: A predefined dictionary maps the predicted disease to a basic home remedy.  
5. **Voice Output**: The result is read aloud using the `gTTS` library.

---

## Tech Stack

- Python  
- Streamlit (for the web app UI)  
- scikit-learn (for model training)  
- gTTS (for text-to-speech)  
- Pandas / CSV (for symptom and disease mapping)  
- Pickle (for model and encoder loading)

## Dataset
The app uses a custom CSV dataset containing one-hot encoded symptoms and disease labels. The model was trained offline and saved as a .pkl file.

## ⚠️Disclaimer
This application is intended for educational and informational purposes only.
It is not a substitute for professional medical advice. Always consult a licensed healthcare provider for accurate diagnosis and treatment.

[Try the ChatDoctor AI](https://chatdoctor-moheethahmed.streamlit.app/)


## Screenshots
<img width="850" height="700" alt="image" src="https://github.com/user-attachments/assets/113d10f7-2f7a-42ed-9c69-c245b4727451" />
<img width="1000" height="700" alt="Screenshot 2025-07-20 155037" src="https://github.com/user-attachments/assets/fe7c39f8-4c4c-43ce-bb57-9576649de182" />
