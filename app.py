from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allows frontend to communicate with backend

# Load your trained ML model
with open('car_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Function to predict car price using the model
def predict_price(year, mileage):
    # Make sure input format matches what your model expects
    X = np.array([[year, mileage]])  # 2D array for single prediction
    price = model.predict(X)[0]     # model.predict returns array
    return round(price, 2)          # Round to 2 decimal places

# API endpoint for prediction
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    year = int(data['year'])
    mileage = float(data['mileage'])
    price = predict_price(year, mileage)
    return jsonify({'price': price})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)