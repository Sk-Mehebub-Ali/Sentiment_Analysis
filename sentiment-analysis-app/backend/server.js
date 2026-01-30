const express = require('express');
const cors = require('cors');
const axios = require('axios');
require('dotenv').config();

const app = express();

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Configuration
const PORT = process.env.PORT || 5000;
const ML_SERVICE_URL = process.env.ML_SERVICE_URL || 'http://localhost:5001';

// Health check endpoint
app.get('/api/health', async (req, res) => {
  try {
    const mlHealth = await axios.get(`${ML_SERVICE_URL}/health`);
    res.json({
      status: 'healthy',
      backend: 'running',
      mlService: mlHealth.data
    });
  } catch (error) {
    res.status(503).json({
      status: 'degraded',
      backend: 'running',
      mlService: 'unavailable',
      error: error.message
    });
  }
});

// Sentiment analysis endpoint
app.post('/api/analyze', async (req, res) => {
  try {
    const { review } = req.body;

    // Validation
    if (!review || typeof review !== 'string') {
      return res.status(400).json({
        error: 'Invalid request',
        message: 'Please provide a review text'
      });
    }

    if (review.trim().length === 0) {
      return res.status(400).json({
        error: 'Empty review',
        message: 'Review text cannot be empty'
      });
    }

    if (review.length > 2000) {
      return res.status(400).json({
        error: 'Review too long',
        message: 'Review must be less than 2000 characters'
      });
    }

    // Call ML service
    console.log(`Analyzing review: "${review.substring(0, 50)}..."`);
    
    const response = await axios.post(`${ML_SERVICE_URL}/predict`, {
      review: review
    }, {
      timeout: 10000 // 10 second timeout
    });

    console.log(`Result: ${response.data.sentiment} (${response.data.confidence}%)`);

    res.json({
      success: true,
      data: response.data
    });

  } catch (error) {
    console.error('Error calling ML service:', error.message);
    
    if (error.code === 'ECONNREFUSED') {
      return res.status(503).json({
        error: 'Service unavailable',
        message: 'ML service is not running. Please start the Python backend.'
      });
    }

    if (error.response) {
      return res.status(error.response.status).json({
        error: 'ML service error',
        message: error.response.data.error || 'An error occurred'
      });
    }

    res.status(500).json({
      error: 'Internal server error',
      message: 'An unexpected error occurred'
    });
  }
});

// Root endpoint
app.get('/', (req, res) => {
  res.json({
    message: 'Sentiment Analysis API',
    version: '1.0.0',
    endpoints: {
      'GET /api/health': 'Check service health',
      'POST /api/analyze': 'Analyze product review sentiment'
    }
  });
});

// 404 handler
app.use((req, res) => {
  res.status(404).json({
    error: 'Not found',
    message: 'The requested endpoint does not exist'
  });
});

// Error handler
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({
    error: 'Internal server error',
    message: err.message
  });
});

// Start server
app.listen(PORT, () => {
  console.log(`✅ Express server running on port ${PORT}`);
  console.log(`📊 API available at http://localhost:${PORT}`);
  console.log(`🤖 ML Service URL: ${ML_SERVICE_URL}`);
});
