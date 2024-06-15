import streamlit as st
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# Function to generate signature using Pillow (PIL)
def generate_signature(name):
    # Customize the signature text
    signature_text = f'Regards,\n{name}'

    # Set image dimensions and background color
    img_width, img_height = 800, 200
    bg_color = (255, 255, 255)  # White background

    # Create a new image with white background
    signature_img = Image.new('RGB', (img_width, img_height), bg_color)

    # Initialize ImageDraw object
    draw = ImageDraw.Draw(signature_img)

    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", size=30)
    except IOError:
        font = ImageFont.load_default()
        st.warning("Font not found, using default font.")

    # Calculate text size and position
    text_width, text_height = draw.textsize(signature_text, font=font)
    text_x = (img_width - text_width) / 2
    text_y = (img_height - text_height) / 2

    # Add text to image
    draw.text((text_x, text_y), signature_text, fill=(0, 0, 0), font=font)

    return signature_img

# CRUD operations functions
def create_data(name):
    data = pd.DataFrame({'Name': [name]})
    return data

def read_data(data):
    return data

def update_data(data, new_name):
    data['Name'] = new_name
    return data

def delete_data(data):
    data = None
    return data

# Main Streamlit app
def main():
    st.title('CRUD Operations and Signature Generator')

    # Sidebar menu
    menu = st.sidebar.selectbox('Menu', ['Create', 'Read', 'Update', 'Delete', 'Generate Signature'])

    if menu == 'Create':
        st.subheader('Create Data')
        name = st.text_input('Enter Name:')
        if st.button('Create'):
            data = create_data(name)
            st.write('Data Created:')
            st.write(data)

    elif menu == 'Read':
        st.subheader('Read Data')
        if 'data' not in st.session_state:
            st.warning('No data available. Please create data first.')
        else:
            st.write('Current Data:')
            st.write(st.session_state.data)

    elif menu == 'Update':
        st.subheader('Update Data')
        if 'data' not in st.session_state:
            st.warning('No data available. Please create data first.')
        else:
            new_name = st.text_input('Enter New Name:')
            if st.button('Update'):
                updated_data = update_data(st.session_state.data, new_name)
                st.write('Data Updated:')
                st.write(updated_data)
                st.session_state.data = updated_data

    elif menu == 'Delete':
        st.subheader('Delete Data')
        if 'data' not in st.session_state:
            st.warning('No data available. Please create data first.')
        else:
            if st.button('Delete'):
                deleted_data = delete_data(st.session_state.data)
                st.write('Data Deleted:')
                st.session_state.data = deleted_data

    elif menu == 'Generate Signature':
        st.subheader('Generate Signature')
        name = st.text_input('Enter Your Name:')
        if st.button('Generate'):
            signature_img = generate_signature(name)
            st.image(signature_img, caption='Generated Signature', use_column_width=True)

# Initialize Streamlit app
if __name__ == '__main__':
    main()
