import replicate
import streamlit as st
from replicate.client import Client
from io import BytesIO
from PIL import Image
import requests

st.set_page_config(page_title="Flux-Schnell Model Demo",
                   page_icon="🎨", layout="wide")

st.title("Dream Canvas 🎨")

REPLICATE_API_TOKEN = st.secrets["REPLICATE_API_TOKEN"]
MODEL = "black-forest-labs/flux-schnell"
client = Client(api_token=REPLICATE_API_TOKEN)

prompt = st.text_input(
    "Type your prompt...",
    value='black forest gateau cake spelling out the words "SETHYBOO", tasty, food photography, dynamic shot',
)

aspect_ratio = st.sidebar.selectbox(
    "Aspect Ratio",
    options=["1:1", "16:9", "21:9", "2:3",
             "3:2", "4:5", "5:4", "9:16", "9:21"],
)

output_format = st.sidebar.selectbox(
    "Select Output Format", options=["webp", "png", "jpg"]
)

output_quality = st.sidebar.slider(
    "Output Quality", min_value=0, max_value=100, value=100
)

if st.button("Generate image", type="primary"):
    output = client.run(
        MODEL,
        input={
            "prompt": prompt,
            "num_outputs": 1,
            "aspect_ratio": aspect_ratio,
            "output_format": output_format,
            "output_quality": output_quality,
        },
    )

    image_url = output[0]
    image = Image.open(BytesIO(requests.get(image_url).content))

    st.image(image, caption=prompt)

    # Prepare the image for download
    img_buffer = BytesIO()
    image.save(img_buffer, format=output_format.upper())
    img_buffer.seek(0)

    # Add download button
    st.download_button(
        label="Download Image",
        data=img_buffer,
        file_name=f"generated_image.{output_format}",
        mime=f"image/{output_format}",
    )
