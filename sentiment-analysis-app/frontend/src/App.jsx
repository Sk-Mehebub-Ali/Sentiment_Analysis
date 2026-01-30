import React, { useState } from 'react';
import './App.css';

function App() {
  const [review, setReview] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!review.trim()) {
      setError('Please enter a review');
      return;
    }

    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await fetch('http://localhost:5000/api/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ review }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.message || 'Failed to analyze review');
      }

      setResult(data.data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleClear = () => {
    setReview('');
    setResult(null);
    setError(null);
  };

  const getSentimentEmoji = (sentiment) => {
    return sentiment === 'POSITIVE' ? '😊' : '😞';
  };

  const getSentimentColor = (sentiment) => {
    return sentiment === 'POSITIVE' ? '#4caf50' : '#f44336';
  };

  return (
    <div className="app">
      <div className="container">
        <header className="header">
          <h1 className="title">
            <span className="emoji">💬</span>
            Product Review Sentiment Analyzer
          </h1>
          <p className="subtitle">
            Analyze the sentiment of product reviews using AI
          </p>
        </header>

        <div className="card">
          <form onSubmit={handleSubmit} className="form">
            <div className="input-group">
              <label htmlFor="review" className="label">
                Enter Product Review
              </label>
              <textarea
                id="review"
                className="textarea"
                placeholder="Type or paste a product review here... (e.g., 'This product is amazing! It works perfectly and exceeded my expectations.')"
                value={review}
                onChange={(e) => setReview(e.target.value)}
                rows="6"
                maxLength="2000"
                disabled={loading}
              />
              <div className="char-count">
                {review.length} / 2000 characters
              </div>
            </div>

            <div className="button-group">
              <button 
                type="submit" 
                className="btn btn-primary"
                disabled={loading || !review.trim()}
              >
                {loading ? (
                  <>
                    <span className="spinner"></span>
                    Analyzing...
                  </>
                ) : (
                  <>
                    <span>🔍</span>
                    Analyze Sentiment
                  </>
                )}
              </button>
              
              {(review || result) && !loading && (
                <button 
                  type="button" 
                  className="btn btn-secondary"
                  onClick={handleClear}
                >
                  Clear
                </button>
              )}
            </div>
          </form>

          {error && (
            <div className="alert alert-error">
              <span className="alert-icon">⚠️</span>
              <div>
                <strong>Error:</strong> {error}
              </div>
            </div>
          )}

          {result && (
            <div className="result-card">
              <h2 className="result-title">Analysis Result</h2>
              
              <div className="sentiment-display">
                <div 
                  className="sentiment-badge"
                  style={{ backgroundColor: getSentimentColor(result.sentiment) }}
                >
                  <span className="sentiment-emoji">
                    {getSentimentEmoji(result.sentiment)}
                  </span>
                  <span className="sentiment-label">
                    {result.sentiment}
                  </span>
                </div>
              </div>

              <div className="confidence-section">
                <div className="confidence-label">
                  <span>Confidence Score</span>
                  <span className="confidence-value">{result.confidence}%</span>
                </div>
                <div className="progress-bar">
                  <div 
                    className="progress-fill"
                    style={{ 
                      width: `${result.confidence}%`,
                      backgroundColor: getSentimentColor(result.sentiment)
                    }}
                  ></div>
                </div>
              </div>

              <div className="review-display">
                <h3 className="review-label">Analyzed Review:</h3>
                <p className="review-text">{result.review}</p>
              </div>
            </div>
          )}
        </div>

        <footer className="footer">
          <p>Powered by AI & Machine Learning 🤖</p>
        </footer>
      </div>
    </div>
  );
}

export default App;
