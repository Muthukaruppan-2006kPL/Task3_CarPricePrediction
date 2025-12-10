from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows frontend to communicate with backend

# Dummy function to predict car price
def predict_price(year, mileage):
    # Replace this with your ML model later
    return (2025 - int(year)) * 1000 + int(mileage) * 0.5

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    year = data['year']
    mileage = data['mileage']
    price = predict_price(year, mileage)
    return jsonify({'price': price})

if __name__ == '__main__':
    app.run(debug=True)