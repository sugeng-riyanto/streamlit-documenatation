import streamlit as st
from streamlit_drawable_canvas import st_canvas
import base64

# Function to convert drawn signature to base64 string
def convert_signature_to_base64(signature_image):
    return base64.b64encode(signature_image).decode('utf-8')

def main():
    st.title('Signature Drawing App')

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
        if drawing_canvas.json_data["objects"]:  # check if there's any drawing
            signature_image = drawing_canvas.image_data[-1]  # get the last drawn image
            st.image(signature_image)
            signature_base64 = convert_signature_to_base64(signature_image)
            st.write('### Signature saved successfully!')
            st.write(f'Base64 representation: `{signature_base64}`')
        else:
            st.write('### No signature drawn yet. Please draw and try again.')

if __name__ == "__main__":
    main()
