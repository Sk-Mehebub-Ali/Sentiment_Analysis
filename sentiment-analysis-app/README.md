# 💬 Product Review Sentiment Analysis App

A full-stack web application that uses machine learning to analyze the sentiment of product reviews. Built with React, Express, Flask, and Hugging Face Transformers.

## 🌟 Features

- **AI-Powered Analysis**: Uses DistilBERT model for accurate sentiment prediction
- **Real-time Results**: Instant sentiment analysis with confidence scores
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Clean UI/UX**: Modern, intuitive interface with smooth animations
- **REST API**: Scalable backend architecture with separate ML service

## 🏗️ Architecture

```
Frontend (React + Vite)
    ↓
Express Backend (Node.js)
    ↓
ML Service (Flask + Transformers)
```

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js** (v16 or higher)
- **Python** (v3.8 or higher)
- **npm** or **yarn**
- **pip** (Python package manager)

## 🚀 Installation & Setup

### Important: Add Your Model First!

**Before running the application**, you need to place your pre-trained model pickle file in the correct location:

1. Navigate to: `backend/ml_service/model/`
2. Place your pickle file(s):
   - `sentiment_model.pkl` (your main model)
   - `vectorizer.pkl` (if you have a separate vectorizer)

📖 **See `PICKLE_MODEL_GUIDE.md` for detailed instructions on using your custom model.**

### Step 1: Clone or Download the Project

If you haven't already, download the project files to your local machine.

### Step 2: Set Up the Python ML Service

Navigate to the ML service directory:

```bash
cd backend/ml_service
```

Create a virtual environment (recommended):

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

### Step 3: Set Up the Express Backend

Open a new terminal and navigate to the backend directory:

```bash
cd backend
```

Install Node.js dependencies:

```bash
npm install
```

### Step 4: Set Up the React Frontend

Open another terminal and navigate to the frontend directory:

```bash
cd frontend
```

Install React dependencies:

```bash
npm install
```

## ▶️ Running the Application

You need to run three services. Open three separate terminal windows:

### Terminal 1: Start the ML Service (Python/Flask)

```bash
cd backend/ml_service
# Activate virtual environment first (if not already active)
python app.py
```

You should see:
```
Loading sentiment analysis model...
Model loaded successfully!
* Running on http://0.0.0.0:5001
```

### Terminal 2: Start the Express Backend

```bash
cd backend
npm start
```

You should see:
```
✅ Express server running on port 5000
📊 API available at http://localhost:5000
🤖 ML Service URL: http://localhost:5001
```

### Terminal 3: Start the React Frontend

```bash
cd frontend
npm run dev
```

You should see:
```
VITE v5.x.x  ready in xxx ms

➜  Local:   http://localhost:3000/
```

### Step 5: Open the Application

Open your browser and navigate to:
```
http://localhost:3000
```

## 🎯 How to Use

1. **Enter a Review**: Type or paste a product review in the text area
2. **Click Analyze**: Press the "Analyze Sentiment" button
3. **View Results**: See the sentiment (Positive/Negative) and confidence score
4. **Try Another**: Click "Clear" to analyze another review

### Example Reviews to Try:

**Positive:**
```
This product is absolutely amazing! It exceeded all my expectations and works perfectly. 
I would highly recommend it to anyone. Great quality and fast shipping!
```

**Negative:**
```
Very disappointed with this purchase. The product arrived damaged and doesn't work as 
described. Poor quality and terrible customer service. Would not recommend.
```

## 🛠️ API Endpoints

### Express Backend (Port 5000)

- `GET /api/health` - Check service health
- `POST /api/analyze` - Analyze review sentiment
  ```json
  Request:
  {
    "review": "Your review text here"
  }
  
  Response:
  {
    "success": true,
    "data": {
      "sentiment": "POSITIVE",
      "confidence": 99.87,
      "review": "Your review text here"
    }
  }
  ```

### ML Service (Port 5001)

- `GET /health` - Health check
- `POST /predict` - Direct sentiment prediction

## 📱 Responsive Design

The application is fully responsive and works on:
- 📱 Mobile phones (320px and up)
- 📱 Tablets (768px and up)
- 💻 Desktops (1024px and up)

## 🔧 Troubleshooting

### Issue: ML Service not starting

**Solution**: Make sure you've activated the virtual environment and installed all requirements:
```bash
cd backend/ml_service
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Issue: "Service unavailable" error

**Solution**: Ensure all three services are running:
1. ML Service on port 5001
2. Express backend on port 5000
3. React frontend on port 3000

### Issue: Port already in use

**Solution**: Change the port in the respective config file:
- ML Service: Change port in `backend/ml_service/app.py`
- Express: Change PORT in `backend/.env`
- React: Change port in `frontend/vite.config.js`

### Issue: CORS errors

**Solution**: Make sure flask-cors is installed in the ML service:
```bash
pip install flask-cors
```

## 📦 Production Deployment

### Build the Frontend

```bash
cd frontend
npm run build
```

This creates an optimized production build in the `dist` folder.

### Deploy Options

- **Frontend**: Deploy to Vercel, Netlify, or any static hosting
- **Backend**: Deploy to Heroku, Railway, or any Node.js hosting
- **ML Service**: Deploy to Python hosting (Heroku, Railway, Google Cloud Run)

**Note**: Update the API URLs in production:
- Frontend: Update the fetch URL to your backend URL
- Backend: Update ML_SERVICE_URL in `.env`

## 🧪 Testing

Test the API directly:

```bash
# Test ML service
curl -X POST http://localhost:5001/predict \
  -H "Content-Type: application/json" \
  -d '{"review": "This product is great!"}'

# Test Express backend
curl -X POST http://localhost:5000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"review": "This product is great!"}'
```

## 🤖 Model Information

- **Model**: Your custom pre-trained sentiment analysis model
- **Format**: Pickle (.pkl) file
- **Framework**: Scikit-learn (or your ML framework)
- **Task**: Binary sentiment classification (Positive/Negative)

The application is designed to work with your own trained model. Simply place your pickle file in `backend/ml_service/model/` directory.

**Note**: The first time you run the ML service, it will load your pickle file. Make sure the file is in the correct location before starting the server.

## 📝 License

MIT License - feel free to use this project for learning or commercial purposes.

## 🙏 Credits

- Model: Hugging Face Transformers
- UI Icons: Unicode Emojis
- Frontend: React + Vite
- Backend: Express.js
- ML Service: Flask + PyTorch

## 💡 Future Enhancements

Potential improvements:
- [ ] Add multi-class sentiment (Very Positive, Positive, Neutral, Negative, Very Negative)
- [ ] Store analysis history
- [ ] Add user authentication
- [ ] Export results to CSV/PDF
- [ ] Batch analysis for multiple reviews
- [ ] Additional NLP metrics (emotion detection, key phrases)

## 📧 Support

If you encounter any issues or have questions, please check the troubleshooting section above or create an issue in the repository.

---

**Enjoy analyzing reviews! 🎉**
