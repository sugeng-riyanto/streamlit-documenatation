import streamlit as st
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': [10, 20, 30, 40]
})

st.title('Displaying DataFrames')
st.write(df)
