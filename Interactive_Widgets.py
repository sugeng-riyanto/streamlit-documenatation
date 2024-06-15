import streamlit as st

st.title('Interactive Widgets Example')

# Slider
number = st.slider('Pick a number', 0, 100)
st.write('The selected number is', number)

# Text Input
name = st.text_input('Enter your name')
st.write('Hello,', name)

# Button
if st.button('Click me'):
    st.write('Button clicked!')
