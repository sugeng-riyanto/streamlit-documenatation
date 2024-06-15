import streamlit as st

def main():
    st.title('Streamlit Forms Example')

    # Text Input
    st.subheader('Text Input')
    name = st.text_input('Enter your name:')
    st.write(f'You entered: {name}')

    # Number Input
    st.subheader('Number Input')
    age = st.number_input('Enter your age:', min_value=0, max_value=150, step=1)
    st.write(f'Your age is: {age}')

    # Date Input
    st.subheader('Date Input')
    birth_date = st.date_input('Enter your birth date:')
    st.write(f'Your birth date is: {birth_date}')

    # Time Input
    st.subheader('Time Input')
    appointment_time = st.time_input('Enter appointment time:')
    st.write(f'Your appointment time is: {appointment_time}')

    # Selectbox
    st.subheader('Selectbox')
    color_options = ['Red', 'Green', 'Blue']
    selected_color = st.selectbox('Select your favorite color:', color_options)
    st.write(f'Your favorite color is: {selected_color}')

    # Multiselect
    st.subheader('Multiselect')
    fruit_options = ['Apple', 'Banana', 'Orange', 'Grape']
    selected_fruits = st.multiselect('Select your favorite fruits:', fruit_options)
    st.write('Your favorite fruits are:')
    for fruit in selected_fruits:
        st.write(f'- {fruit}')

    # Checkbox
    st.subheader('Checkbox')
    agree_terms = st.checkbox('I agree to the terms and conditions')
    if agree_terms:
        st.write('You agreed to the terms and conditions')

    # Button to submit form
    if st.button('Submit'):
        st.subheader('Form Submission Result')
        st.write(f'Name: {name}')
        st.write(f'Age: {age}')
        st.write(f'Birth Date: {birth_date}')
        st.write(f'Appointment Time: {appointment_time}')
        st.write(f'Favorite Color: {selected_color}')
        st.write('Favorite Fruits:')
        for fruit in selected_fruits:
            st.write(f'- {fruit}')
        if agree_terms:
            st.write('You agreed to the terms and conditions')

if __name__ == '__main__':
    main()
