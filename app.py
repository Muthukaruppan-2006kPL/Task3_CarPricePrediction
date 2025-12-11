from flask import Flask, render_template, request
import numpy as np
import joblib
import pickle
import os

app = Flask(__name__)

# -----------------------------
# Load Model Safely
# -----------------------------
model = None

# Try joblib first
if os.path.exists("car_price_model.pkl"):
    try:
        model = joblib.load("car_price_model.pkl")
        print("Model loaded using joblib")
    except:
        try:
            model = pickle.load(open("car_price_model.pkl", "rb"))
            print("Model loaded using pickle")
        except Exception as e:
            print("Model load error:", e)

# If model not found
if model is None:
    raise Exception("Model file 'car_price_model.pkl' not loaded. Check filename!")


# -----------------------------
# Routes
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        year = int(request.form['year'])
        present_price = float(request.form['present_price'])
        kms_driven = int(request.form['kms_driven'])
        owner = int(request.form['owner'])
        fuel_type = request.form['fuel_type']
        seller_type = request.form['seller_type']
        transmission = request.form['transmission']

        # Encoding fuel
        if fuel_type == 'Petrol':
            fuel_Petrol = 1
            fuel_Diesel = 0
        else:
            fuel_Petrol = 0
            fuel_Diesel = 1

        # Encoding seller
        if seller_type == 'Individual':
            seller_Individual = 1
        else:
            seller_Individual = 0

        # Encoding transmission
        if transmission == 'Manual':
            transmission_Manual = 1
        else:
            transmission_Manual = 0

        # Arrange input
        input_data = np.array([[year, present_price, kms_driven, owner,
                                fuel_Diesel, fuel_Petrol, seller_Individual,
                                transmission_Manual]])

        # Predict
        prediction = model.predict(input_data)[0]
        output = round(prediction, 2)

        return render_template("index.html", prediction_text=f"Predicted Car Price: ₹{output} Lakhs")

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {e}")


if __name__ == "__main__":
    app.run(debug=True)