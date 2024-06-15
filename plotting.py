import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Title
st.title('Matplotlib Chart in Streamlit')

# Data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Matplotlib Figure
fig, ax = plt.subplots()
ax.plot(x, y)

# Display the chart
st.pyplot(fig)
