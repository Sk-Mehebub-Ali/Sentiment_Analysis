# Quick Start Guide

## 🚀 Get Running in 5 Minutes

### Prerequisites Check
```bash
node --version  # Should be v16+
python --version  # Should be 3.8+
```

### Installation

**1. Install Python Dependencies**
```bash
cd backend/ml_service
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**2. Install Node Dependencies**
```bash
# Backend
cd ../../backend
npm install

# Frontend
cd ../frontend
npm install
```

### Running the App

Open 3 terminals and run:

**Terminal 1 - ML Service:**
```bash
cd backend/ml_service
source venv/bin/activate  # Windows: venv\Scripts\activate
python app.py
```

**Terminal 2 - Express Backend:**
```bash
cd backend
npm start
```

**Terminal 3 - React Frontend:**
```bash
cd frontend
npm run dev
```

### Access the App
Open http://localhost:3000 in your browser!

## 🎯 Testing

Try these sample reviews:

**Positive:**
"This product is amazing! Highly recommend it. Great quality and fast delivery."

**Negative:**
"Very disappointed. Product broke after one day. Waste of money."

## ⚡ Common Issues

**ML Service won't start?**
- Make sure virtual environment is activated
- Run: `pip install -r requirements.txt`

**Backend connection error?**
- Ensure all 3 services are running
- Check ports: ML (5001), Backend (5000), Frontend (3000)

**CORS error?**
- Make sure flask-cors is installed
- Restart the ML service

---

For detailed documentation, see README.md
