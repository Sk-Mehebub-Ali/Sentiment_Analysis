# Project Structure

```
sentiment-analysis-app/
│
├── README.md                      # Comprehensive documentation
├── QUICKSTART.md                  # Quick start guide
├── .gitignore                     # Git ignore file
│
├── frontend/                      # React Frontend (Port 3000)
│   ├── src/
│   │   ├── App.jsx               # Main React component
│   │   ├── App.css               # Responsive styles
│   │   ├── main.jsx              # React entry point
│   │   └── index.css             # Global styles
│   ├── index.html                # HTML template
│   ├── package.json              # Frontend dependencies
│   └── vite.config.js            # Vite configuration
│
└── backend/                       # Backend Services
    │
    ├── server.js                  # Express Server (Port 5000)
    ├── package.json               # Backend dependencies
    ├── .env                       # Environment variables
    │
    └── ml_service/                # Python ML Service (Port 5001)
        ├── app.py                 # Flask API + ML model
        └── requirements.txt       # Python dependencies
```

## File Descriptions

### Frontend Files
- **App.jsx**: Main React component with sentiment analysis UI
- **App.css**: Responsive CSS with mobile-first design
- **main.jsx**: React application entry point
- **vite.config.js**: Vite bundler configuration

### Backend Files
- **server.js**: Express REST API that routes requests to ML service
- **.env**: Configuration (ports, ML service URL)

### ML Service Files
- **app.py**: Flask server with Hugging Face Transformers model
- **requirements.txt**: Python packages (Flask, Transformers, PyTorch)

## Tech Stack

**Frontend:**
- React 18
- Vite (build tool)
- CSS3 with responsive design

**Backend:**
- Node.js + Express
- Axios for HTTP requests

**ML Service:**
- Python + Flask
- Hugging Face Transformers
- DistilBERT model

## Ports

- Frontend: 3000
- Express Backend: 5000
- ML Service: 5001
