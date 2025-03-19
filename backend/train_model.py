import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Dummy dataset (replace with actual dataset)
data = pd.DataFrame({
    'rank': [1000, 5000, 10000, 20000, 30000],
    'cutoff': [90, 85, 75, 60, 50]
})

# Split dataset
X = data[['rank']]
y = data['cutoff']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
with open("backend/cutoff_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved successfully!")
