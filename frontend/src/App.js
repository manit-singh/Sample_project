import React, { useState } from "react";

function App() {
  const [inputData, setInputData] = useState({
    rank: "",
  });

  const [prediction, setPrediction] = useState(null);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    setInputData({ ...inputData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Basic validation for rank
      if (isNaN(inputData.rank) || parseInt(inputData.rank) <= 0) {
        throw new Error("Invalid rank. Please enter a positive integer.");
      }

      const response = await fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          rank: parseInt(inputData.rank)
        }),
      });

      if (!response.ok) {
        throw new Error("Failed to fetch prediction");
      }

      const data = await response.json();
      setPrediction(data.predicted_cutoff);
      setError(null); // Clear any previous error
    } catch (error) {
      console.error("Error fetching prediction:", error);
      setError(error.message); // Display error message to user
      setPrediction(null); // Clear prediction on error
    }
  };

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h1>Cutoff Predictor</h1>
      <form onSubmit={handleSubmit} style={{ display: "inline-block", textAlign: "left" }}>
        <label>Rank: </label>
        <input type="number" name="rank" value={inputData.rank} onChange={handleChange} required />
        <br />
        <button type="submit">Predict Cutoff</button>
      </form>

      {prediction !== null && (
        <div style={{ marginTop: "20px" }}>
          <h2>Predicted Cutoff: {prediction}</h2>
        </div>
      )}

      {error && (
        <div style={{ marginTop: "20px", color: "red" }}>
          <h2>Error: {error}</h2>
        </div>
      )}
    </div>
  );
}

export default App;

