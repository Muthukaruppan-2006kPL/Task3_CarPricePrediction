from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__,static_folder='static')

# Load Model
model = pickle.load(open("car_price_model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    name = request.form['name']
    year = int(request.form['year'])
    km_driven = int(request.form['km_driven'])
    fuel = request.form['fuel']
    seller_type = request.form['seller_type']
    transmission = request.form['transmission']
    owner = request.form['owner']

    new_data = pd.DataFrame({
        "name": [name],
        "year": [year],
        "km_driven": [km_driven],
        "fuel": [fuel],
        "seller_type": [seller_type],
        "transmission": [transmission],
        "owner": [owner]
    })

    prediction = model.predict(new_data)[0]

    prediction = max(0, prediction)

    return render_template("index.html", result=round(prediction, 2))


if __name__ == "__main__":
    app.run(debug=True)