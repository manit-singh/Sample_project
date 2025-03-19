from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open("backend/cutoff_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET"])
def home():
    return "Cutoff Prediction API is Running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        rank = np.array([[data["rank"]]])
        predicted_cutoff = model.predict(rank).tolist()
        return jsonify({"predicted_cutoff": predicted_cutoff})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
