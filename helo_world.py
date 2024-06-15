import streamlit as st

st.title('Hello World!')
st.write("This is my first Streamlit app.")
with st.sidebar:
    st.write('This is a sidebar')

with st.expander('Expand'):
    st.write('This is expandable')