from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load your model
model = pickle.load(open("car_price_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        year = int(request.form.get("year"))
        km_driven = int(request.form.get("km"))
        fuel = int(request.form.get("fuel"))
        seller = int(request.form.get("seller"))
        transmission = int(request.form.get("transmission"))
        owner = int(request.form.get("owner"))

        features = np.array([[year, km_driven, fuel, seller, transmission, owner]])
        prediction = model.predict(features)[0]

        return render_template("index.html", result=round(prediction, 2))

    except Exception as e:
        return render_template("index.html", result=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)