import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title('My first Streamlit app')

# Markdown
st.markdown('Hello, *World!* :sunglasses:')

# Data
df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['col1', 'col2'])

# Display DataFrame
st.write(df)

# Line Chart
st.line_chart(df)
