from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

#load pickel file 
model = pickle.load(open("model2.pkl", "rb"))
scaler = pickle.load(open("scaler2.pkl", "rb"))
columns = pickle.load(open("columns2.pkl", "rb"))

@app.route("/")
def home():
    return "Churn Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        
        #convert input into dataframe 
        df = pd.DataFrame([data])
        df = df[columns]
        
        #scale
        df_scaled = scaler.transform(df)
        
        #predict
        prediction = model.predict(df_scaled)
        probability = model.predict_proba(df_scaled)[0][1]  # churn probability

        return jsonify({
            "prediction": int(prediction[0]),
            "probability": float(probability)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        })

if __name__ == "__main__":
    app.run(debug=True)