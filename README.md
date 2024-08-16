# Dream Canvas 🎨

Dream Canvas is a Streamlit web application that leverages the Flux-Schnell AI model to generate images based on text prompts. This application allows users to create unique, AI-generated images by simply describing what they want to see.

## Features

- Text-to-image generation using the Flux-Schnell model
- Customizable aspect ratios for generated images
- Multiple output formats (webp, png, jpg)
- Adjustable output quality
- One-click image download

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/tonykipkemboi/replicate-flux-schnell-model-demo.git
   cd replicate-flux-schnell-model-demo
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Replicate API token:

   - Create a `.streamlit/secrets.toml` file in the project root
   - Check out the `secrets_example.toml` file for the correct format example
   - Add your Replicate API token to the file `.streamlit/secrets.toml`:

     ```toml
     REPLICATE_API_TOKEN="your-api-token-here"
     ```

## Usage

1. Run the Streamlit app:

   ```python
   streamlit run demo.py
   ```

2. Open your web browser and navigate to the provided local URL (usually `http://localhost:8501`).

3. Enter your desired image prompt in the text area.

4. Customize the aspect ratio, output format, and quality using the sidebar options.

5. Click the "Generate" button to create your image.

6. Once generated, you can view the image and download it using the provided button.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgements

- [Replicate](https://replicate.com/) for providing the AI model API
- [Streamlit](https://streamlit.io/) for the web app framework
- [Flux-Schnell](https://replicate.com/black-forest-labs/flux-schnell) model by Black Forest Labs
