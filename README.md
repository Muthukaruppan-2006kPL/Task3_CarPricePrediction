🚗 Car Price Prediction using Machine Learning

This project predicts the selling price of used cars based on various features such as brand, year, kilometers driven, fuel type, transmission type, and more.
A Linear Regression model is used to analyze the patterns and make accurate price predictions.

📌 Table of Contents

📘 Project Overview

📂 Dataset Details

🛠️ Technologies Used

⚙️ Project Workflow

🤖 Machine Learning Model

📊 Results

💻 How to Run

📁 Project Structure

📸 Output Screenshots

📝 License

📘 Project Overview

Used car prices vary based on many factors such as brand, model, mileage, and year.
This project uses Linear Regression to build a model that can predict car prices based on historical data.

The process includes:

Data collection

Cleaning & preprocessing

Feature engineering

Model training

Evaluation

Predictions

📂 Dataset Details

File: cardekho.csv
Source: CarDekho (Used Cars Dataset)

Dataset contains columns like:

Year

Selling_Price

Present_Price

Driven_kms

Fuel_Type

Seller_Type

Transmission

Owner

🛠️ Technologies Used

Python

Pandas

NumPy

Matplotlib

Seaborn

Scikit-Learn

Jupyter Notebook

⚙️ Project Workflow

Load and explore the dataset

Handle missing values

Convert categorical features using encoding

Split data into training and testing sets

Train the Linear Regression model

Evaluate using metrics (MAE, MSE, RMSE)

Save the model (pickle file)

Make predictions

🤖 Machine Learning Model
Linear Regression Model

This model finds the best-fit line that maps the relationship between car features and selling price.

Why Linear Regression?
✔ Simple and interpretable
✔ Works well on numerical datasets
✔ Good baseline model for regression problems

Model file: car_price_model.pkl

📊 Results

Your model was successfully trained using Linear Regression.

Typical evaluation metrics:

MAE – Average error in prediction

MSE – Squared error

RMSE – Root mean squared error

(You can add your exact values here if needed.)

💻 How to Run
1️⃣ Clone the repository
git clone https://github.com/Muthukaruppan-2006kPL/Task3_CarPricePrediction.git

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the notebook

Open:

car_price_prediction.ipynb

4️⃣ To load the model:
import pickle

model = pickle.load(open("car_price_model.pkl", "rb"))

📁 Project Structure
│── car_price_prediction.ipynb
│── car_price_model.pkl
│── cardekho.csv
│── requirements.txt
│── README.md
│── .gitignore

📸 Output Screenshots

(Add your model results, plots, or sample prediction images here.)
Example:

images/
   ├── scatter_plot.png
   ├── heatmap.png

📝 License

This project is part of the CodeAlpha Internship – Machine Learning Tasks.
Feel free to use and modify it for educational purposes.
