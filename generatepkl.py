import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train the model
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# Save the model to a file
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)
