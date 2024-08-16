import streamlit as st
from replicate.client import Client
from io import BytesIO
from PIL import Image
import requests


def main():
    st.set_page_config(
        page_title="Flux-Schnell Model Demo",
        page_icon="🎨",
        layout="wide"
    )

    st.title("Dream Canvas 🎨")

    replicate_api_token = st.secrets["REPLICATE_API_TOKEN"]
    model = "black-forest-labs/flux-schnell"
    client = Client(api_token=replicate_api_token)

    prompt = st.text_area(
        "Type your prompt...",
        value='black forest gateau cake spelling out the words "SETHYBOO", tasty, food photography, dynamic shot',
    )

    aspect_ratio = st.sidebar.selectbox(
        "Aspect Ratio",
        options=["1:1", "16:9", "21:9", "2:3",
                 "3:2", "4:5", "5:4", "9:16", "9:21"],
    )

    output_format = st.sidebar.selectbox(
        "Select Output Format", options=["png", "jpg", "webp"]
    )

    output_quality = st.sidebar.slider(
        "Output Quality", min_value=0, max_value=100, value=90
    )

    _, col2, _ = st.columns(3)

    with col2:
        if st.button("📸 Generate Image", type="primary", use_container_width=True):
            generate_and_display_image(
                client, model, prompt, aspect_ratio, output_format, output_quality)


def generate_and_display_image(client, model, prompt, aspect_ratio, output_format, output_quality):
    output = client.run(
        model,
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
        use_container_width=True,
    )


if __name__ == "__main__":
    main()
