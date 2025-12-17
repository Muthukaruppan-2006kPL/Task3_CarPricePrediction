from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("car_price_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        year = int(request.form["year"])
        km_driven = int(request.form["km_driven"])

        fuel = request.form["fuel"]
        seller = request.form["seller"]
        transmission = request.form["transmission"]
        owner = request.form["owner"]

        fuel_petrol = 1 if fuel == "Petrol" else 0
        fuel_diesel = 1 if fuel == "Diesel" else 0

        seller_individual = 1 if seller == "Individual" else 0

        transmission_manual = 1 if transmission == "Manual" else 0

        owner_first = 1 if owner == "First Owner" else 0
        owner_second = 1 if owner == "Second Owner" else 0

        input_data = np.array([[year, km_driven,
                                fuel_diesel, fuel_petrol,
                                seller_individual,
                                transmission_manual,
                                owner_first, owner_second]])

        prediction = model.predict(input_data)[0]

        return render_template(
            "index.html",
            prediction_text=f"₹ {round(prediction, 2)}"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text="Error occurred"
        )

if __name__ == "__main__":
    app.run(debug=True)