from kokoro import KPipeline
from IPython.display import display, Audio
import soundfile as sf
import numpy as np

# pipeline
pipeline = KPipeline(lang_code='b')

# text
text = "fuck off man"

# Generate audio
audios = [audio for _, _, audio in pipeline(text, voice='af_heart')]

# Combine all chunks
full_audio = np.concatenate(audios)

# Save and play
sf.write("kokoro.wav", full_audio, 24000)
display(Audio(data=full_audio, rate=24000))
