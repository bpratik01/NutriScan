import os
import streamlit as st
from PIL import Image
from inference import img2text

st.title("Image to Nutrition Information")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if st.button("Generate Nutrient Values") and uploaded_file is not None:
    image = Image.open(uploaded_file)
    image_path = "temp_image.jpg"
    image.save(image_path)
    
    description, nutrient_values, full_response = img2text(image_path)

    if description == "Error":
        st.error(f"Error: {nutrient_values} - {full_response}")
    else:
        st.markdown(f"**Image Description:** {description}")
        st.markdown(f"**Nutrient Values:** {nutrient_values}")
        st.markdown("**Full Response:**")
        st.code(full_response, language='json')
    
    # Remove the temporary image file after processing
    os.remove(image_path)
else:
    st.warning("Please upload an image.")