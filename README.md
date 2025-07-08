# Next Word Prediction Project

## Overview
This project consists of two main components:
1. A Machine Learning model for next word prediction
2. A Web Application that provides an interactive interface for the prediction model

## Machine Learning Component
- Implemented in `next-word-prediction.ipynb`
- Uses LSTM neural network for sequence prediction
- Trained on Sherlock Holmes text corpus
- Saves trained model and tokenizer for use in the web app

## Web Application
- Built using Python Flask
- Provides a text input interface that shows word predictions
- Features:
  - Real-time prediction as you type
  - Keyboard shortcuts for accepting suggestions
  - Clean, responsive UI

## Getting Started
1. Install requirements:
```
pip install -r requirements.txt
```
2. Run the web app:
```
flask run
```
3. Access the application at `http://localhost:5000`

## Project Structure
```
.
├── MachineLearning/
│   ├── next-word-prediction.ipynb  # Jupyter notebook with model training
│   ├── model/                    # Saved model and tokenizer
│   └── data/                     # Training data
└── WebApp/
    ├── app.py                    # Flask application
    ├── static/                   # CSS and JavaScript
    └── templates/                # HTML templates
```

## Requirements
- Python 3.11+
- TensorFlow
- Flask
- NumPy

## License
MIT