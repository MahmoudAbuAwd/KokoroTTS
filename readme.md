# Kokoro TTS Project

A Python implementation using the Kokoro Text-to-Speech (TTS) model for high-quality speech synthesis.

## Overview

This project demonstrates how to use the Kokoro TTS model to convert text into natural-sounding speech. Kokoro is a state-of-the-art neural text-to-speech system that produces high-quality audio output.

## Features

- High-quality text-to-speech conversion
- Multiple voice options
- Audio output in WAV format
- Real-time audio playback in Jupyter notebooks
- Customizable sampling rate (24kHz)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/MahmoudAbuAwd/KokoroTTS
cd kokoro-tts
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Dependencies

- `kokoro` - The main TTS library
- `soundfile` - For audio file I/O
- `numpy` - For numerical operations
- `IPython` - For Jupyter notebook audio display

## Usage

### Main.py

```python
from kokoro import KPipeline
from IPython.display import display, Audio
import soundfile as sf
import numpy as np

# Initialize the pipeline
pipeline = KPipeline(lang_code='b')

# Your text to convert
text = "Hello, this is a test of the Kokoro TTS system."

# Generate audio
audios = [audio for _, _, audio in pipeline(text, voice='af_heart')]

# Combine all audio chunks
full_audio = np.concatenate(audios)

# Save to file
sf.write("output.wav", full_audio, 24000)

# Play in Jupyter notebook
display(Audio(data=full_audio, rate=24000))
```

### Voice Options

The system supports different voice profiles. In the example above, we use `'af_heart'`. You can experiment with different voices by changing this parameter.

### Language Codes

The pipeline accepts different language codes. In this example, we use `'b'` as the language code.

## Project Structure

```
kokoro-tts/
├── examples/
│   └── basic_usage.py
├── kokoro_tts/
│   ├── __pycache__/
│   ├── core.py
│   └── init.py
├── output/
│   ├── hello.wav
│   └── new.wav
├── streamlit/
│   └── app.py
├── .gitattributes
├── .gitignore
├── LICENSE
├── main.py
├── python-version
├── README.md
└── requirements.txt
```

## Configuration

### Audio Settings

- **Sample Rate**: 24,000 Hz (24kHz)
- **Output Format**: WAV
- **Audio Processing**: Chunks are concatenated for seamless playback

### Pipeline Parameters

- `lang_code`: Language code for the TTS model
- `voice`: Voice profile selection
- `text`: Input text for synthesis

## Examples

### Example 1: Basic Text-to-Speech

```python
pipeline = KPipeline(lang_code='b')
text = "Welcome to Kokoro TTS!"
audios = [audio for _, _, audio in pipeline(text, voice='af_heart')]
full_audio = np.concatenate(audios)
sf.write("welcome.wav", full_audio, 24000)
```

### Example 2: Longer Text Processing

```python
long_text = """
This is a longer piece of text that demonstrates 
the capabilities of the Kokoro TTS system for 
processing extended content.
"""

pipeline = KPipeline(lang_code='b')
audios = [audio for _, _, audio in pipeline(long_text, voice='af_heart')]
full_audio = np.concatenate(audios)
sf.write("long_text.wav", full_audio, 24000)
```

## Output

The generated audio files are saved in WAV format with the following specifications:
- Sample rate: 24,000 Hz
- Format: WAV
- Quality: High-fidelity speech synthesis

## Streamlit App

The project includes a Streamlit web application for easy interaction with the TTS system. Run it with:

```bash
streamlit run streamlit/app.py
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the terms specified in the LICENSE file.

### Performance Tips

- For longer texts, consider processing in smaller chunks
- Adjust the sample rate if needed for your specific use case
- Use appropriate voice profiles for your target audience

## Support

For issues and questions, please refer to the project's issue tracker or documentation.
