from IPython.display import display, Audio
import soundfile as sf
import numpy as np

class KokoroTTS:
    def __init__(self, lang_code='b'):
        """
        Initialize the Kokoro TTS pipeline.
        
        Args:
            lang_code (str): Language code (default 'b')
        """
        from kokoro import KPipeline
        self.pipeline = KPipeline(lang_code=lang_code)
        
    def generate(self, text, voice='af_heart'):
        """
        Generate audio from text.
        
        Args:
            text (str): Text to convert to speech
            voice (str): Voice to use (default 'af_heart')
            
        Returns:
            AudioResult: Audio result object with playback and save methods
        """
        audios = [audio for _, _, audio in self.pipeline(text, voice=voice)]
        full_audio = np.concatenate(audios)
        return AudioResult(full_audio, 24000)

class AudioResult:
    def __init__(self, audio_data, sample_rate):
        self.audio_data = audio_data
        self.sample_rate = sample_rate
        
    def play(self):
        """Play the audio in Jupyter notebook."""
        display(Audio(data=self.audio_data, rate=self.sample_rate))
        
    def save(self, filename):
        """Save the audio to a file.
        
        Args:
            filename (str): Output filename (e.g., 'output.wav')
        """
        sf.write(filename, self.audio_data, self.sample_rate)