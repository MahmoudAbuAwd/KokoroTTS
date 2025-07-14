import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))  # Add project root to path
from kokoro_tts.core import KokoroTTS

tts = KokoroTTS(lang_code='b')
audio = tts.generate("hello my name is mahmoud abuawd , i live in amman /jordan , i have becalour degree in ai & robotics", voice='af_heart')
audio.play()
audio.save("hello.wav")