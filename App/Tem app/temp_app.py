from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# 1. Load saved files
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

# 2. Home route
@app.route("/")
def home():
    return "Churn Prediction API is running!"

# 3. Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input
        data = request.json

        # Convert to DataFrame
        input_data = pd.DataFrame([data])
        input_data = input_data[columns]
        print(columns)

        # Scaling
        input_scaled = scaler.transform(input_data)

        # Prediction
        prediction = model.predict(input_scaled)

        return jsonify({
            "prediction": int(prediction[0])
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        })

# 4. Run app
if __name__ == "__main__":
    app.run(debug=True)