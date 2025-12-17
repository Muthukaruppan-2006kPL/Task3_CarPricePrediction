from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load model
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

        input_df = pd.DataFrame([{
            "name": "Maruti",
            "year": year,
            "km_driven": km_driven,
            "fuel": fuel,
            "seller_type": seller,
            "transmission": transmission,
            "owner": owner
        }])

        prediction = model.predict(input_df)[0]
        prediction = round(prediction, 2)

        return render_template(
            "index.html",
            prediction_text=f"₹ {prediction}"
        )

    except Exception as e:
        print(e)
        return render_template(
            "index.html",
            prediction_text="Error occurred"
        )

if __name__ == "__main__":
    app.run(debug=True)