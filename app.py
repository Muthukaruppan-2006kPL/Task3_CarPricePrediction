from flask import Flask, request, jsonify, render_template
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
    data = request.json

    df = pd.DataFrame([{
        "name": data["name"],
        "year": data["year"],
        "km_driven": data["km_driven"],
        "fuel": data["fuel"],
        "seller_type": data["seller_type"],
        "transmission": data["transmission"],
        "owner": data["owner"]
    }])

    result = model.predict(df)[0]

    return jsonify({"predicted_price": max(0, round(result, 2))})

if __name__ == "__main__":
    app.run(debug=True)