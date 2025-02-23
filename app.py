import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import sequence
import pickle

# Streamlit Page Config
st.set_page_config(
    page_title="🎬 Sentiment Analyzer",
    page_icon="🎭",
    layout="centered"
)

# Load Custom CSS
def local_css():
    st.markdown("""
    <style>
    .main-header {
        color: #2c3e50;
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 20px;
        background: linear-gradient(to right, #ff5733, #ffbd69);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .subheader {
        color: #34495e;
        text-align: center;
        margin-bottom: 20px;
    }
    .stTextArea>div>div>textarea {
    width: 100%;
    height: 150px;
    border-radius: 8px;
    border: 2px solid #ff5733;
    padding: 12px;
    font-size: 1rem;
    background-color: #f7f9fc;
    color: #2c3e50;
    caret-color: #ff5733; /* Ensures cursor is visible */
    outline: none; /* Removes default focus outline */
}

.stTextArea>div>div>textarea::placeholder {
    color: #95a5a6;
    font-style: italic;
}

    }
    .stButton>button {
        background-color: #ff5733;
        color: white;
        border: none;
        padding: 12px 20px;
        border-radius: 5px;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton>button:hover {
        background-color: #c0392b;
        transform: scale(1.05);
        box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.15);
    }
    .result-box {
        background-color: #f7f9fc;
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #e0e0e0;
        margin-top: 20px;
        text-align: center;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    }
    .emoji {
        font-size: 3rem;
        text-align: center;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Load the Tokenizer
try:
    with open('tokenizer.pkl', 'rb') as f:
        word_index = pickle.load(f)
except Exception as e:
    st.error(f"Error loading tokenizer: {e}")
    st.stop()

# Load Model
try:
    model = tf.keras.models.load_model('SimpleRnn_imdb.h5')
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Function to preprocess text
def preprocess_text(text):
    words = text.lower().split()
    encoded_review = [word_index.get(word, 2) + 3 for word in words]
    padded_review = sequence.pad_sequences([encoded_review], maxlen=500)  
    return padded_review

# Prediction Function
def predict_sentiment(review):
    preprocessed_input = preprocess_text(review)
    prediction = model.predict(preprocessed_input)[0][0]

    if prediction >= 0.6:
        sentiment = 'Positive'
        emoji = "😊"
    elif prediction <= 0.4:
        sentiment = 'Negative'
        emoji = "😠"
    else:
        sentiment = 'Neutral'
        emoji = "😐"

    return sentiment, float(prediction), emoji  

# Streamlit UI
def main():
    local_css()  

    st.markdown('<div class="main-header">🎬 Sentiment Analyzer</div>', unsafe_allow_html=True)
    st.markdown('<div class="subheader">Analyze the sentiment of your movie review!</div>', unsafe_allow_html=True)

    # Improved Styled Text Area
    st.markdown('<p style="font-size:18px; font-weight:bold; color:#2c3e50;">📝 Write Your Movie Review Below:</p>', unsafe_allow_html=True)

    user_input = st.text_area(
        "",
        placeholder="Type your thoughts about the movie here...",
        height=150,
        max_chars=500,
        key="review_input"
    )

    if st.button("Analyze Sentiment"):
        if user_input:
            sentiment, score, emoji = predict_sentiment(user_input)

            # Display Results
            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.subheader(f"🎯 Sentiment: {sentiment} {emoji}")
            st.write(f"**Confidence Score:** `{score:.4f}`")

            # Display Progress Bar
            progress_val = score if sentiment == "Positive" else 1 - score
            st.progress(progress_val)

            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.warning("⚠️ Please enter a review before analyzing.")

# Run the App
if __name__ == "__main__":
    main()
