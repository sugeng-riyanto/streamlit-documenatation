import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import base64
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from io import BytesIO
            # Send email with signature
sender_email = 'shsmodernhill@shb.sch.id'  # Replace with your email
sender_password = 'jvvmdgxgdyqflcrf'  # Replace with your email password (secure handling advised)
# Define a DataFrame to store signatures
signature_df = pd.DataFrame(columns=['Full Name', 'Signature'])

# Function to convert drawn signature to base64 string
def convert_signature_to_base64(signature_image):
    buffered = Image.fromarray(signature_image.astype('uint8'))
    img_buffer = BytesIO()
    buffered.save(img_buffer, format="JPEG")
    signature_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
    return signature_base64

def send_email(sender_email, sender_password, recipient_email, subject, body, attachment=None):
    try:
        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        # Attach body and attachment
        message.attach(MIMEText(body, 'plain'))

        if attachment:
            # Attach signature image
            image = MIMEImage(base64.b64decode(attachment))
            image.add_header('Content-Disposition', 'attachment', filename='signature.jpeg')
            message.attach(image)

        # Create SMTP session
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send email
        server.sendmail(sender_email, recipient_email, message.as_string())
        server.quit()

        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

def main():
    st.title('Signature Drawing App')

    menu = ['Draw Signature', 'View Signatures']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Draw Signature':
        # Full name input
        full_name = st.text_input('Full Name')

        # Canvas to draw the signature
        drawing_canvas = st_canvas(
            fill_color="rgb(0, 0, 0)",  # Fixed color for the drawing canvas
            stroke_width=5,
            stroke_color="rgb(255, 255, 255)",
            background_color="rgb(0, 128, 128)",
            update_streamlit=True,
            height=200,
            width=500,
            drawing_mode="freedraw",
            key="canvas",
        )

        # Save button to save the signature
        if st.button('Save Signature'):
            if full_name.strip() == '':
                st.warning('Please enter a full name.')
            elif drawing_canvas.json_data["objects"]:  # check if there's any drawing
                signature_image = drawing_canvas.image_data[-1]  # get the last drawn image
                signature_base64 = convert_signature_to_base64(signature_image)

                # Save to DataFrame
                global signature_df
                signature_df = signature_df.append({'Full Name': full_name, 'Signature': signature_base64}, ignore_index=True)
                st.success(f'Signature saved successfully for {full_name}!')

            else:
                st.warning('No signature drawn yet. Please draw and try again.')

    elif choice == 'View Signatures':
        st.title('View Signatures')
        if signature_df.empty:
            st.info('No signatures saved yet.')
        else:
            for index, row in signature_df.iterrows():
                st.subheader(f'Signature for {row["Full Name"]}')
                signature_image = base64.b64decode(row["Signature"])
                st.image(signature_image, use_column_width=True)

    # Email sending section
    st.sidebar.header('Send Signature via Email')
    sender_email = st.sidebar.text_input('Your Email')
    sender_password = st.sidebar.text_input('Your Email Password', type='password')
    recipient_email = st.sidebar.text_input('Recipient Email')
    if st.sidebar.button('Send Email'):
        if sender_email and sender_password and recipient_email:
            if signature_df.empty:
                st.warning('No signatures to send. Please draw and save a signature first.')
            else:
                for index, row in signature_df.iterrows():
                    signature_base64 = row["Signature"]
                    if send_email(sender_email, sender_password, recipient_email, 'Signed Document', f'Hello, {row["Full Name"]}!\n\nPlease find attached the signed document.', signature_base64):
                        st.sidebar.success(f'Signature sent successfully to {recipient_email}!')
                    else:
                        st.sidebar.error('Failed to send email. Please check your credentials and try again.')
        else:
            st.sidebar.warning('Please fill in all email fields.')

if __name__ == "__main__":
    main()
