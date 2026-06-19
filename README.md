# 🎬 Movie Review Sentiment Analyzer

## 📌 Project Overview
An end-to-end Machine Learning web application built to instantly analyze the sentiment of movie reviews. The model processes raw text, cleans it, and predicts whether the review is **Positive** or **Negative** using a trained machine learning algorithm.

## 🚀 Live Demo
[Insert Your Streamlit App Link Here]

## 🛠️ Tech Stack
* **Language:** Python
* **Machine Learning:** Scikit-learn (LinearSVC, TF-IDF Vectorization)
* **Data Processing:** Pandas, Regular Expressions (re)
* **Frontend/UI:** Streamlit
* **Model Serialization:** Joblib

## 🧠 Model Workflow
1. **Text Preprocessing:** Removes HTML tags, numbers, and punctuation, then converts text to lowercase.
2. **Vectorization:** Transforms the cleaned text into numerical features using `TfidfVectorizer`.
3. **Classification:** A `LinearSVC` model trained on the IMDB dataset predicts the sentiment.

## 💻 How to Run Locally
1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2.Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

	
