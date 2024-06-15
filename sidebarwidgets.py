import streamlit as st

st.title('Sidebar Example')

# Slider in the sidebar
sidebar_slider = st.sidebar.slider('Sidebar Slider', 0, 100)
st.write('Slider value:', sidebar_slider)

# Text input in the sidebar
sidebar_text = st.sidebar.text_input('Sidebar Text Input', 'Type here...')
st.write('Text input value:', sidebar_text)

# Button in the sidebar
if st.sidebar.button('Sidebar Button'):
    st.write('Button clicked!')
