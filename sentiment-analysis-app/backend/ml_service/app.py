import joblib
import logging
import os
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Globals
lr_model = None
tfidf = None

# ✅ PATHS ONLY (strings)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "sentiment_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "tfidf_vectorizer.pkl")



def load_model():
    global lr_model, tfidf

    try:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"{MODEL_PATH} not found")

        if not os.path.exists(VECTORIZER_PATH):
            raise FileNotFoundError(f"{VECTORIZER_PATH} not found")

        logger.info(f"Loading model from {MODEL_PATH}...")
        lr_model = joblib.load(MODEL_PATH)

        logger.info(f"Loading vectorizer from {VECTORIZER_PATH}...")
        tfidf = joblib.load(VECTORIZER_PATH)

        logger.info("✅ All models loaded successfully!")
        return True

    except Exception as e:
        logger.error(f"Error loading model: {e}")
        lr_model = None
        tfidf = None
        return False

def predict_sentiment(review_text):
    if lr_model is None or tfidf is None:
        raise RuntimeError("Model or vectorizer not loaded")

    text_features = tfidf.transform([review_text])
    prediction = lr_model.predict(text_features)[0]

    if hasattr(lr_model, "predict_proba"):
        confidence = max(lr_model.predict_proba(text_features)[0]) * 100
    else:
        confidence = 100.0

    sentiment = "POSITIVE" if prediction == 1 else "NEGATIVE"

    return {
        "sentiment": sentiment,
        "confidence": round(confidence, 2)
    }

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': lr_model is not None,
        'vectorizer_loaded': tfidf is not None
    })

@app.route('/predict', methods=['POST'])
def predict_sentiment_endpoint():
    """
    Predict sentiment for a product review
    Expected JSON: {"review": "text of the review"}
    """
    try:
        if lr_model is None or tfidf is None:
            return jsonify({
                'error': 'Model not loaded',
                'message': 'Please ensure sentiment_model.pkl and tfidf_vectorizer.pkl are in the ml_service directory'
            }), 500
        
        # Get review text from request
        data = request.get_json()
        
        if not data or 'review' not in data:
            return jsonify({
                'error': 'No review text provided'
            }), 400
        
        review_text = data['review'].strip()
        
        if not review_text:
            return jsonify({
                'error': 'Review text is empty'
            }), 400
        
        # Truncate if too long
        if len(review_text) > 2000:
            review_text = review_text[:2000]
        
        # Perform sentiment analysis
        logger.info(f"Analyzing review: {review_text[:50]}...")
        result = predict_sentiment(review_text)
        
        # Format response
        response = {
            'sentiment': result['sentiment'],
            'confidence': result['confidence'],
            'review': review_text
        }
        
        logger.info(f"Prediction: {result['sentiment']} ({result['confidence']:.2f}%)")
        
        return jsonify(response), 200
        
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        return jsonify({
            'error': 'An error occurred during prediction',
            'details': str(e)
        }), 500

@app.route('/', methods=['GET'])
def index():
    """Root endpoint"""
    return jsonify({
        'message': 'Sentiment Analysis ML Service (Custom Model)',
        'model_loaded': lr_model is not None,
        'vectorizer_loaded': tfidf is not None,
        'endpoints': {
            '/health': 'GET - Health check',
            '/predict': 'POST - Predict sentiment'
        }
    })

if __name__ == '__main__':
    # Load the model
    if not load_model():
        logger.warning("="*60)
        logger.warning("⚠️  MODEL NOT LOADED!")
        logger.warning("Please place these files in backend/ml_service/:")
        logger.warning(f"  - {MODEL_PATH}")
        logger.warning(f"  - {VECTORIZER_PATH}")
        logger.warning("="*60)
    else:
        logger.info("="*60)
        logger.info("✅ All models loaded successfully!")
        logger.info("="*60)
    
    # Start the server
    app.run(host='0.0.0.0', port=5001, debug=True)
