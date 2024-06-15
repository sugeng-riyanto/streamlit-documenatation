import streamlit as st
import pandas as pd
from io import BytesIO
from PIL import Image
from PyPDF2 import PdfReader

st.title('File Upload and Display Example')

# File upload section
file_type = st.selectbox("Select file type", ["Image", "CSV", "Text", "PDF"])

if file_type == "Image":
    uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

elif file_type == "CSV":
    uploaded_file = st.file_uploader("Upload a CSV file...", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write('Uploaded DataFrame:')
        st.write(df)

elif file_type == "Text":
    uploaded_file = st.file_uploader("Upload a text file...", type=["txt"])
    if uploaded_file is not None:
        # Handle text file upload correctly
        text_string = uploaded_file.read().decode("utf-8")
        st.write('Uploaded Text:')
        st.write(text_string)

elif file_type == "PDF":
    uploaded_file = st.file_uploader("Upload a PDF file...", type=["pdf"])
    if uploaded_file is not None:
        # Handle PDF file upload correctly
        pdf_reader = PdfReader(uploaded_file)
        num_pages = len(pdf_reader.pages)
        st.write(f'Number of Pages: {num_pages}')

        # Extract text from all pages
        pdf_text = ''
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            pdf_text += page.extract_text()

        st.write('Extracted Text:')
        st.write(pdf_text)
