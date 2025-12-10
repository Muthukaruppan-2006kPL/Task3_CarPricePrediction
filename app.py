from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allows frontend to communicate with backend

# Load your trained ML model
model = joblib.load('car_price_model.pkl')

# Function to predict car price using all features
def predict_price(features):
    X = np.array([features])  # Convert to 2D array
    price = model.predict(X)[0]
    return round(price, 2)

# API endpoint for prediction
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Collect all 13 features in the order your model expects
    features = [
        int(data['year']),
        float(data['mileage']),
        int(data['brand_encoded']),
        int(data['fuel_encoded']),
        int(data['transmission_encoded']),
        int(data['owner_encoded']),
        float(data['engine']),
        float(data['power']),
        float(data['seats']),
        int(data['location_encoded']),
        float(data['some_feature_11']),
        float(data['some_feature_12']),
        float(data['some_feature_13'])
    ]

    price = predict_price(features)
    return jsonify({'price': price})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)