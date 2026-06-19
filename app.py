import streamlit as st
import joblib
import re

st.set_page_config(page_title="Movie Review Analyzer", page_icon="🎬", layout="centered")

def clean_text(text):
    text = re.sub(r'<.*?>', ' ', text)
    text = re.sub(r'[^a-zA-Z]', ' ', text).lower()
    return text

@st.cache_resource
def load_models():
    model = joblib.load('model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
    return model, vectorizer

model, vectorizer = load_models()

st.title("🎬 Movie Review Sentiment Analyzer")
st.markdown("### Instantly analyze the sentiment of any movie review!")
st.write("Enter your movie review in the text box below, and the machine learning model will predict whether it is positive or negative.")

user_input = st.text_area("Enter your review:", placeholder="Type a movie review here...", height=150)

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter a review first!")
    else:
    
        cleaned_input = clean_text(user_input)
        vectorized_input = vectorizer.transform([cleaned_input])
        prediction = model.predict(vectorized_input)[0]

    
        st.divider() 
        if prediction == 'positive':
            st.success("✨ This is a **Positive** Review!")
        else:
            st.error("😡 This is a **Negative** Review!")