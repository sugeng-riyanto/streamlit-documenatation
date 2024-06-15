import streamlit as st
from reportlab.pdfgen import canvas
from io import BytesIO
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Function to send email
def send_email(to_email, subject, body, attachment_data):
    from_email = 'shsmodernhill@shb.sch.id'  # Replace with your email address
    password ='jvvmdgxgdyqflcrf' 

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    if attachment_data:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment_data.getvalue())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment', filename='drawing.pdf')
        msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

# Function to generate PDF from drawing
def generate_pdf_from_drawing(drawing_data):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)

    # Set up PDF size (adjust as necessary)
    pdf.setPageSize((600, 200))

    # Draw each stroke in the PDF
    for stroke in drawing_data:
        points = stroke['points']
        pdf.moveTo(points[0][0], points[0][1])
        for point in points[1:]:
            pdf.lineTo(point[0], point[1])
        pdf.drawPath()

    pdf.save()
    buffer.seek(0)
    return buffer

def main():
    st.title('Email Signature and Attachment Sender')

    # Input fields
    full_name = st.text_input('Enter your full name:')
    signature = st.text_area('Create your email signature:', height=100)
    to_email = st.text_input('Recipient email address:')

    # Drawing canvas for PDF attachment (HTML + JavaScript)
    st.subheader('Create PDF Attachment')
    drawing_html = """
    <canvas id="canvas" width="600" height="200"></canvas>
    <button onclick="savePDF()">Save as PDF</button>
    <script>
    var canvas = document.getElementById('canvas');
    var ctx = canvas.getContext('2d');
    var isDrawing = false;
    var points = [];

    canvas.addEventListener('mousedown', function(e) {
        isDrawing = true;
        points.push({ x: e.offsetX, y: e.offsetY });
    });

    canvas.addEventListener('mousemove', function(e) {
        if (isDrawing) {
            points.push({ x: e.offsetX, y: e.offsetY });
            draw();
        }
    });

    canvas.addEventListener('mouseup', function() {
        isDrawing = false;
    });

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.beginPath();
        ctx.moveTo(points[0].x, points[0].y);
        for (var i = 1; i < points.length; i++) {
            ctx.lineTo(points[i].x, points[i].y);
        }
        ctx.stroke();
    }

    function savePDF() {
        var pdfCanvas = document.createElement('canvas');
        pdfCanvas.width = 600;
        pdfCanvas.height = 200;
        var pdfCtx = pdfCanvas.getContext('2d');

        pdfCtx.fillStyle = '#ffffff';
        pdfCtx.fillRect(0, 0, pdfCanvas.width, pdfCanvas.height);
        pdfCtx.drawImage(canvas, 0, 0);

        var pdfData = pdfCanvas.toDataURL('image/png');
        var doc = new jsPDF();
        doc.addImage(pdfData, 'PNG', 10, 10, 180, 100);
        var pdfBytes = doc.output();
        
        var blob = new Blob([pdfBytes], { type: 'application/pdf' });
        var url = URL.createObjectURL(blob);
        
        var a = document.createElement('a');
        a.href = url;
        a.download = 'drawing.pdf';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    }
    </script>
    """
    st.markdown(drawing_html, unsafe_allow_html=True)

    # Send email button
    if st.button('Send Email'):
        if to_email == '':
            st.error('Please enter recipient email address.')
        else:
            subject = f"Email from {full_name}"
            body = f"Hello,\n\n{signature}\n\nRegards,\n{full_name}"

            # Capture drawing data from JavaScript canvas
            st.warning('Please download the PDF by clicking "Save as PDF" button before sending the email.')

            # Simulate sending email with a placeholder
            st.success(f'Email sent successfully to {to_email}!')

if __name__ == '__main__':
    main()
