# Import libraries
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load Excel dataset (from Day 4)
df = pd.read_excel("reviews.xlsx")  # Make sure the file is in the same folder
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.write(df)
# Prepare data
X = df['review']           # reviews column
y = df['sentiment']        # sentiment column (1=Positive, 0=Negative)

# Convert text to numbers
vectorizer = CountVectorizer()
X_vector = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_vector, y)

# --- Streamlit App Starts Here ---

# Set web page title
st.set_page_config(page_title="Movie Review Sentiment Analyzer")

# App heading
st.title("🎬 Movie Review Sentiment Analyzer")

# Input box
review = st.text_area("Enter your movie review:")

# Predict button
if st.button("Predict"):
    if review.strip() == "":
        st.warning("Please enter a review first.")
    else:
        # Vectorize and predict
        review_vector = vectorizer.transform([review])
        result = model.predict(review_vector)[0]
        confidence = model.predict_proba(review_vector).max()

        # Display result with emoji and confidence
        if result == 1:
            st.success("Sentiment: Positive 😊")
            st.write("Great! Your review is positive.")
        else:
            st.error("Sentiment: Negative 😞")
            st.write("Oops! That sounds like a negative review.")

        st.write(f"Confidence Score: {confidence:.2f}")
