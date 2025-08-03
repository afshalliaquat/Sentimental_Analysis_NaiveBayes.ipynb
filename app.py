import streamlit as st
import joblib

model = joblib.load("model_LR_bow.pkl")
vectorizer = joblib.load("vectorizer.pkl")

label_map = {
    0: 'sadness',
    1: 'anger',
    2: 'love',
    3: 'surprise',
    4: 'fear',
    5: 'joy'
}

st.set_page_config(page_title="Sentiment Analyzer",page_icon = "🧠",layout="wide")

st.markdown("""
    <style>
    body {
        background: linear-gradient(120deg, #e3f2fd, #ffffff);
    }

    .block-container {
        margin: auto;
        padding: 2rem;
        max-width: 90%;
        min-height: 660px;  /* Keeps the container height fixed even before prediction */
        background: white;
        border-radius: 20px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease-in-out;
    }

    .stTextArea textarea {
        font-size: 18px;
        font-family: 'Segoe UI', sans-serif;
        padding: 1rem;
        border-radius: 8px;
    }

    .emotion-title {
        font-size: 20px;
        font-weight: bold;
        color: #1565c0;
        text-align: center;
        margin-top: 1rem;
    }

    .emoji {
        font-size: 68px;
        text-align: center;
        margin-top: 1.5rem;
    }
    h1 {
        font-size: 56px !important;
        text-align: center;
        margin-bottom: 0.5rem;
        color: #0d47a1;
    }

    #MainMenu, footer, header {
        visibility: hidden;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>🎯 Sentiment Analyzer</h1>",  unsafe_allow_html=True)
st.markdown("<p style='font-size: 20px; text-align: center; margin-bottom: 2rem; color: #333;'>Enter a sentence to detect the emotion using machine learning.</p>", unsafe_allow_html=True)

text = st.text_area("✍️ Enter your sentence here:", height=160)

if st.button("🔍 Predict"):
    if text.strip() == "":
        st.warning("⚠️ Please enter a valid sentence.")
    else:
        X = vectorizer.transform([text])
        pred = model.predict(X)[0]
        emotion = label_map[pred]
        emoji_dict = {
            'sadness': "😢", 'anger': "😠", 'love': "❤️",
            'surprise': "😲", 'fear': "😨", 'joy': "😊"
        }

        st.markdown(f"<div class='emoji'>{emoji_dict.get(emotion, '')}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='emotion-title'>Predicted Emotion: <strong>{emotion.capitalize()}</strong></div>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.caption("Developed by Afshal Liaquat | [GitHub](https://github.com/afshalliaquat)")
