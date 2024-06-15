import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import base64
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from io import BytesIO  # For handling byte streams

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

    # Full name input (optional)
    full_name = st.text_input('Full Name (optional)')

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

    # Email input
    recipient_email = st.text_input('Recipient Email')

    # Checkbox for agreeing to terms (optional)
    agree_terms = st.checkbox('I agree to the terms and conditions (optional)')

    # Save button to save and send the signature
    if st.button('Save and Send Signature'):

        if drawing_canvas.json_data["objects"]:  # check if there's any drawing
            signature_image = drawing_canvas.image_data[-1]  # get the last drawn image

            # Convert image to base64
            signature_base64 = convert_signature_to_base64(signature_image)

            # Send email with signature
            sender_email = 'shsmodernhill@shb.sch.id'  # Replace with your email
            sender_password = 'jvvmdgxgdyqflcrf'  # Replace with your email password (secure handling advised)

            if send_email(sender_email, sender_password, recipient_email, 'Signed Document', f'Hello, {full_name or "Recipient"}!\n\nPlease find attached the signed document.', signature_base64):
                st.success(f'Signature sent successfully to {recipient_email}!')
            else:
                st.error('Failed to send email. Please check your credentials and try again.')

            st.image(signature_image)
            st.write(f'Base64 representation: `{signature_base64}`')
        else:
            st.warning('No signature drawn yet. Please draw and try again.')

if __name__ == "__main__":
    main()
