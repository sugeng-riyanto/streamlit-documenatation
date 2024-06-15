import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

st.title('Iris Flower Prediction')

# Input fields
sepal_length = st.number_input('Sepal Length')
sepal_width = st.number_input('Sepal Width')
petal_length = st.number_input('Petal Length')
petal_width = st.number_input('Petal Width')

# Prediction
if st.button('Predict'):
    input_data = pd.DataFrame({
        'sepal_length': [sepal_length],
        'sepal_width': [sepal_width],
        'petal_length': [petal_length],
        'petal_width': [petal_width]
    })
    prediction = model.predict(input_data)
    st.write(f'The predicted class is: {prediction[0]}')

# To run this script, ensure you have a pre-trained model saved as 'model.pkl'.
