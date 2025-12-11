from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import numpy as np
import pickle

app = Flask(__name__)
CORS(app)

# Load model only once
model = pickle.load(open('car_price_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    features = np.array([[ 
        float(data['year']),
        float(data['mileage']),
        float(data['brand_encoded']),
        float(data['fuel_encoded']),
        float(data['transmission_encoded']),
        float(data['owner_encoded']),
        float(data['engine']),
        float(data['power']),
        float(data['seats']),
        float(data['location_encoded']),
        float(data['some_feature_11']),
        float(data['some_feature_12']),
        float(data['some_feature_13'])
    ]])

    prediction = model.predict(features)[0]

    # avoid negative price
    if prediction < 0:
        prediction = 0

    return jsonify({'price': round(prediction, 2)})

if __name__ == '__main__':
    app.run(debug=True)