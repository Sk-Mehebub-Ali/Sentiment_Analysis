# Using Your Custom Pickle Model

This guide explains how to use your pre-trained sentiment analysis model (pickle file) with this application.

## 📁 Model File Structure

You need to place your pickle file(s) in the correct location:

```
backend/
└── ml_service/
    ├── app.py
    ├── requirements.txt
    └── model/              ← CREATE THIS FOLDER
        ├── sentiment_model.pkl      ← YOUR MAIN MODEL FILE
        └── vectorizer.pkl           ← YOUR VECTORIZER (if separate)
```

## 🔧 Setup Instructions

### Step 1: Create the Model Directory

Navigate to the ML service folder and create a `model` directory:

```bash
cd backend/ml_service
mkdir model
```

### Step 2: Place Your Pickle Files

Copy your pickle file(s) into the `model` directory:

**If you have one pickle file (model with built-in preprocessing):**
```bash
# Copy and rename your file to sentiment_model.pkl
cp /path/to/your/model.pkl model/sentiment_model.pkl
```

**If you have two pickle files (separate model and vectorizer):**
```bash
# Copy your model file
cp /path/to/your/model.pkl model/sentiment_model.pkl

# Copy your vectorizer file
cp /path/to/your/vectorizer.pkl model/vectorizer.pkl
```

### Step 3: Customize the Prediction Function (if needed)

The `app.py` file includes a `predict_sentiment()` function that needs to match your model's format.

**Common Model Output Formats:**

1. **Binary Classification (0/1)**
   - 0 = Negative, 1 = Positive
   - Already handled in the code ✅

2. **Binary Classification (-1/1)**
   - Update the code:
   ```python
   sentiment = "POSITIVE" if prediction == 1 else "NEGATIVE"
   ```

3. **String Output ('positive'/'negative')**
   - Already handled in the code ✅

4. **Multi-class (0/1/2 for negative/neutral/positive)**
   - Update the code:
   ```python
   if prediction == 0:
       sentiment = "NEGATIVE"
   elif prediction == 1:
       sentiment = "NEUTRAL"
   else:
       sentiment = "POSITIVE"
   ```

### Step 4: Customize Text Preprocessing (if needed)

If your model requires specific preprocessing (like removing stopwords, stemming, etc.), update the `preprocess_text()` function in `app.py`:

```python
def preprocess_text(text):
    """
    Preprocess the review text
    Modify based on your training preprocessing
    """
    import re
    from nltk.corpus import stopwords
    from nltk.stem import PorterStemmer
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    # Add your custom preprocessing here
    # Examples:
    # - Remove stopwords
    # - Stemming/Lemmatization
    # - Remove URLs, emails, etc.
    
    return text
```

## 🧪 Testing Your Model

### Test via Command Line

```bash
# Start the ML service
python app.py

# In another terminal, test it:
curl -X POST http://localhost:5001/predict \
  -H "Content-Type: application/json" \
  -d '{"review": "This product is amazing!"}'
```

Expected response:
```json
{
  "sentiment": "POSITIVE",
  "confidence": 95.5,
  "review": "This product is amazing!"
}
```

### Test via Python Script

Create a test file `test_model.py`:

```python
import requests

url = "http://localhost:5001/predict"

# Test positive review
positive_review = "This product is amazing! Highly recommended."
response = requests.post(url, json={"review": positive_review})
print("Positive:", response.json())

# Test negative review
negative_review = "Terrible product. Waste of money. Very disappointed."
response = requests.post(url, json={"review": negative_review})
print("Negative:", response.json())
```

## 🔍 Troubleshooting

### Issue 1: "Model file not found"

**Solution:**
- Verify the file path: `backend/ml_service/model/sentiment_model.pkl`
- Check file name is exactly `sentiment_model.pkl`
- Ensure you're in the correct directory

### Issue 2: "Error loading model"

**Solution:**
- Check if pickle file is corrupted:
  ```python
  import pickle
  with open('model/sentiment_model.pkl', 'rb') as f:
      model = pickle.load(f)
  print("Model loaded successfully!")
  ```
- Verify Python version compatibility (pickle files can be version-specific)

### Issue 3: Wrong predictions

**Solution:**
- Check if preprocessing matches your training preprocessing
- Verify the prediction label mapping in `predict_sentiment()`
- Print `raw_prediction` to debug

### Issue 4: "numpy" or "sklearn" not found

**Solution:**
```bash
pip install scikit-learn numpy pandas
```

## 📝 Model Information Template

It's helpful to document your model details. Create a `MODEL_INFO.md` file:

```markdown
# Model Information

## Model Details
- Algorithm: [e.g., Logistic Regression, Random Forest, SVM]
- Training Data: [e.g., Amazon Reviews, IMDB]
- Features: [e.g., TF-IDF, Count Vectorizer]
- Accuracy: [e.g., 92%]

## Preprocessing Steps
1. Convert to lowercase
2. Remove special characters
3. [Your other steps]

## Prediction Format
- Input: String (review text)
- Output: 0 (Negative) or 1 (Positive)
- Confidence: Probability score

## Example Usage
```python
# Input
review = "Great product!"

# Output
{
  "sentiment": "POSITIVE",
  "confidence": 98.5
}
```
```

## 🚀 Next Steps

Once your model is loaded and working:

1. ✅ Test with various reviews
2. ✅ Verify predictions match expected results
3. ✅ Start the full application (frontend + backend)
4. ✅ Test through the web interface

## 💡 Alternative: Multiple Models

If you have multiple pickle files or want to switch between models, you can:

1. Store multiple models in the `model` directory
2. Add model selection logic:

```python
import os

# List available models
MODELS = {
    'v1': 'model/sentiment_model_v1.pkl',
    'v2': 'model/sentiment_model_v2.pkl',
}

# Select model
MODEL_VERSION = os.getenv('MODEL_VERSION', 'v1')
MODEL_PATH = MODELS[MODEL_VERSION]
```

3. Set environment variable:
```bash
export MODEL_VERSION=v2
python app.py
```

---

Need help? Check the main README.md or create an issue!
