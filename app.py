from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

@app.route('/')
def home():
    return "Car Price Prediction API is running"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array([[
        data['year'],
        data['mileage'],
        data['brand_encoded'],
        data['fuel_encoded'],
        data['transmission_encoded'],
        data['owner_encoded'],
        data['engine'],
        data['power'],
        data['seats'],
        data['location_encoded'],
        data['some_feature_11'],
        data['some_feature_12'],
        data['some_feature_13']
    ]])

    model = pickle.load(open('model.pkl', 'rb'))
    prediction = model.predict(features)[0]

    if prediction < 0:
        prediction = 0

    return jsonify({'price': prediction})

        

if __name__ == '__main__':
    app.run(debug=True)