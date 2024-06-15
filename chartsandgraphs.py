import streamlit as st
import pandas as pd
import numpy as np

# Sample data
data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['a', 'b', 'c']
)

st.title('Charts and Graphs')

# Line chart
st.line_chart(data)

# Area chart
st.area_chart(data)

# Bar chart
st.bar_chart(data)
