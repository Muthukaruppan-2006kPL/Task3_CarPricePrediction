from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json

        # Read input EXACTLY as sent from frontend
        features = [
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
        ]

        # Dummy prediction logic
        result = sum(features) * 1000

        # Remove negative values
        if result < 0:
            result = 0

        return jsonify({'price': round(result, 2)})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)