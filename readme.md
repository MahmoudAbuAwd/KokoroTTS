# Kokoro TTS

Kokoro TTS is a powerful and easy-to-use text-to-speech library for Python. It provides a simple interface to convert text into natural-sounding speech using a variety of pre-trained models. The project also includes a Streamlit-based web interface for interactive demonstrations.

## Features

- **High-Quality Speech Synthesis**: Generates clear and natural-sounding audio.
- **Multiple Voices**: Supports a variety of male and female voices.
- **Simple Python API**: Easy to integrate into your Python projects.
- **Interactive Web Demo**: Comes with a Streamlit application for easy testing and demonstration.
- **Customizable Audio**: Allows for adjustment of audio parameters like sample rate.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/kokoro-tts.git
   cd kokoro-tts
   ```

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Python Library

You can use the `KokoroTTS` class to generate speech in your Python scripts. Here's a basic example:

```python
from kokoro_tts.core import KokoroTTS

# Initialize the TTS pipeline
tts = KokoroTTS(lang_code='b')

# Text to be converted to speech
text = "Hello, this is a test of the Kokoro text-to-speech model."

# Generate audio
audio = tts.generate(text, voice='af_heart')

# Play the audio (in a Jupyter environment)
audio.play()

# Save the audio to a file
audio.save("output.wav")
```

### Streamlit Web Demo

The project includes an interactive web demo built with Streamlit. To run it:

1. **Navigate to the Streamlit directory**:
   ```bash
   cd streamlit
   ```

2. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

This will open a web interface in your browser where you can enter text, select a voice, and generate speech in real-time.

## Available Voices

Kokoro TTS offers a selection of male and female voices:

### Female Voices
- `af_heart`
- `af_sky`
- `af_tessa`
- `af_alloy`
- `af_sarah`

### Male Voices
- `am_daniel`
- `am_jamie`
- `am_matthew`
- `am_mike`
- `am_sam`

## License

This project is licensed under the terms of the LICENSE file. Please see the `LICENSE` file for more details.
