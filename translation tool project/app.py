import streamlit as st # type: ignore
from googletrans import Translator
from gtts import gTTS

translator = Translator()

# Page config
st.set_page_config(page_title="Translator", page_icon="🌍", layout="centered")

# 🔥 DARK MODE STYLE + ANIMATION
st.markdown("""
    <style>
    body {
        background-color: #0E1117;
        color: white;
    }
    .stTextArea textarea {
        background-color: #262730;
        color: white;C
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 18px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #4CAF50;
        animation: fadeIn 2s ease-in;
    }
    @keyframes fadeIn {
        0% {opacity: 0;}
        100% {opacity: 1;}
    }
    </style>
""", unsafe_allow_html=True)

# Title with animation
st.markdown('<div class="title">🌍 Language Translator</div>', unsafe_allow_html=True)

# Input
text = st.text_area("Enter text to translate:")

# Languages
languages = {
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese": "zh-cn"
}

col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox("From", list(languages.keys()))

with col2:
    target_lang = st.selectbox("To", list(languages.keys()))

# Translate button
if st.button("✨ Translate"):
    if text:
        with st.spinner("🔄 Translating..."):
            translated = translator.translate(
                text,
                src=languages[source_lang],
                dest=languages[target_lang]
            )

        st.success("✅ Done!")
        st.write(translated.text)

        # Copy-style box
        st.code(translated.text)

        # 🔊 Voice output
        tts = gTTS(translated.text)
        tts.save("output.mp3")
        st.audio("output.mp3")

    else:
        st.warning("⚠ Please enter text")
