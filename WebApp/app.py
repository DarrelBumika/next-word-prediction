from flask import Flask, render_template, request, jsonify
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

# Load model and tokenizer
model = load_model('.\\model\\model.h5')
with open('.\\model\\tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.json['text']
    
    # Tokenize input text
    token_list = tokenizer.texts_to_sequences([text])[0]
    token_list = pad_sequences([token_list], maxlen=18-1, padding='pre')
    
    # Get predictions
    predictions = model.predict(token_list, verbose=0)[0]
    
    # Get top 5 predictions
    top_indices = predictions.argsort()[-5:][::-1]
    top_predictions = [
        {'word': word, 'probability': float(predictions[idx])}
        for word, idx in tokenizer.word_index.items() 
        if idx in top_indices
    ]
    
    return jsonify({'predictions': top_predictions})

if __name__ == '__main__':
    app.run(debug=True)