from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS

app = Flask(__name__, static_folder='../client/build/static', template_folder='../client/build')
CORS(app)  # Allow frontend requests

# Load the trained model
import os
model_path = os.path.join(os.path.dirname(__file__), "cutoff_model.pkl")
if os.path.exists(model_path):
    with open(model_path, "rb") as f:
        model = pickle.load(f)
else:
    raise FileNotFoundError(f"Model file not found at {model_path}")

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        if "rank" not in data:
            return jsonify({"error": "Missing 'rank' in request"}), 400
        
        rank = np.array([[data["rank"]]])
        predicted_cutoff = model.predict(rank).tolist()
        return jsonify({"predicted_cutoff": predicted_cutoff})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Serve static files directly
@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('../client/build/static', path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
