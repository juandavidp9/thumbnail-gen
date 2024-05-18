import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from PIL import Image
import io

def generate_thumbnail(image, size):
    thumbnail = image.resize(size)
    return thumbnail


def main():
    st.markdown("<h1 style='text-align: center;'>Thumbnail Generator</h1>", unsafe_allow_html=True)
    add_vertical_space(3)
    uploaded_file = st.file_uploader("Upload your image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:

        image = Image.open(uploaded_file)
        original_width, original_height = image.size
        st.write(f"Original Size: {original_width} x {original_height} pixels")
        add_vertical_space(1)
        st.image(image, caption="Original Image")
        thumbnail_width = st.slider("Thumbnail Width", 10, original_width, 100)
        thumbnail_height = st.slider("Thumbnail Height", 10, original_height, 80)
        thumbnail_size = (thumbnail_width, thumbnail_height)

               
        thumbnail = generate_thumbnail(image, thumbnail_size)
        st.image(thumbnail, caption="Preview Thumbnail")
        add_vertical_space(1)

        output_format = st.selectbox("Choose Image Format", ("PNG", "JPG"))
        file_name = st.text_input("Enter file name", value="thumbnail")
        image_stream = io.BytesIO()
        if output_format.lower() == "png":
            thumbnail.save(image_stream, format="PNG", quality=100)
        else:
            thumbnail.save(image_stream, format="JPEG", quality=100)
        image_stream.seek(0)
        data = image_stream.getvalue()
        add_vertical_space(1)

        st.download_button(
            label="Download Thumbnail",
            data=data,
            file_name=file_name + "." + output_format.lower(),
            mime=output_format.lower(),
        )

if __name__ == "__main__":
    main()

