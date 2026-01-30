"""
Example: How to Train and Save a Sentiment Analysis Model as Pickle

This is a reference script showing how to create a simple sentiment model
and save it as a pickle file that works with this application.

NOTE: This is just an example. You should use YOUR OWN trained model!
"""

import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Example training data (replace with your actual dataset)
reviews = [
    # Positive reviews
    "This product is amazing! Highly recommend it.",
    "Excellent quality and fast shipping. Love it!",
    "Best purchase I've made this year. Five stars!",
    "Great value for money. Very satisfied.",
    "Perfect! Exactly what I needed.",
    "Outstanding product. Will buy again.",
    "Superb quality. Exceeded my expectations.",
    "Fantastic! Worth every penny.",
    # Negative reviews
    "Terrible product. Waste of money.",
    "Very disappointed. Does not work as advertised.",
    "Poor quality. Broke after one day.",
    "Would not recommend. Customer service is awful.",
    "Horrible experience. Requesting a refund.",
    "Cheaply made. Not worth the price.",
    "Completely useless. Don't buy this.",
    "Worst purchase ever. Total scam.",
]

labels = [
    # 1 for positive, 0 for negative
    1, 1, 1, 1, 1, 1, 1, 1,  # positive
    0, 0, 0, 0, 0, 0, 0, 0,  # negative
]

# Step 1: Create and train the vectorizer
print("Training vectorizer...")
vectorizer = TfidfVectorizer(max_features=1000, ngram_range=(1, 2))
X = vectorizer.fit_transform(reviews)

# Step 2: Train the model
print("Training model...")
model = LogisticRegression(random_state=42)
model.fit(X, labels)

# Step 3: Test the model
print("\nTesting model...")
test_reviews = [
    "This is great! Love it.",
    "Terrible quality. Very bad."
]
test_features = vectorizer.transform(test_reviews)
predictions = model.predict(test_features)
probabilities = model.predict_proba(test_features)

for review, pred, prob in zip(test_reviews, predictions, probabilities):
    sentiment = "POSITIVE" if pred == 1 else "NEGATIVE"
    confidence = max(prob) * 100
    print(f"Review: '{review}'")
    print(f"Prediction: {sentiment} (Confidence: {confidence:.2f}%)")
    print()

# Step 4: Save the model and vectorizer as pickle files
print("Saving model files...")

# Create model directory if it doesn't exist
import os
os.makedirs('model', exist_ok=True)

# Save the model
with open('model/sentiment_model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("✅ Model saved to: model/sentiment_model.pkl")

# Save the vectorizer
with open('model/vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)
print("✅ Vectorizer saved to: model/vectorizer.pkl")

print("\n" + "="*60)
print("SUCCESS! Your model files are ready to use.")
print("Copy them to: backend/ml_service/model/")
print("="*60)

# Optional: Test loading the saved files
print("\nTesting saved files...")
with open('model/sentiment_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

with open('model/vectorizer.pkl', 'rb') as f:
    loaded_vectorizer = pickle.load(f)

# Test with loaded model
test_text = "This product is excellent!"
test_features = loaded_vectorizer.transform([test_text])
prediction = loaded_model.predict(test_features)[0]
probability = loaded_model.predict_proba(test_features)[0]

print(f"Test with loaded model:")
print(f"Input: '{test_text}'")
print(f"Output: {prediction}")
print(f"Confidence: {max(probability)*100:.2f}%")
print("\n✅ Loaded model works correctly!")
