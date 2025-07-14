import streamlit as st
import numpy as np
import soundfile as sf
import tempfile
import os
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Kokoro TTS Demo",
    page_icon="🎤",
    layout="wide"
)

# Title and description
st.title("🎤 Kokoro Text-to-Speech Demo")
st.markdown("Convert text to speech using the Kokoro TTS model")

# Initialize session state
if 'pipeline' not in st.session_state:
    st.session_state.pipeline = None
    st.session_state.model_loaded = False

# Model loading function
@st.cache_resource
def load_model():
    try:
        from kokoro import KPipeline
        pipeline = KPipeline(lang_code='b')
        return pipeline, True
    except Exception as e:
        return None, str(e)

# Load model
if not st.session_state.model_loaded:
    with st.spinner("Loading Kokoro model..."):
        pipeline, status = load_model()
        if isinstance(status, bool) and status:
            st.session_state.pipeline = pipeline
            st.session_state.model_loaded = True
            st.success("Model loaded successfully!")
        else:
            st.error(f"Failed to load model: {status}")
            st.stop()

# Main interface
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Text Input")
    text_input = st.text_area(
        "Enter text to convert to speech:",
        value="Hello, this is a test of the Kokoro text-to-speech model.",
        height=100
    )

with col2:
    st.subheader("Voice Settings")
    
    # Voice selection
    voice_options = [
        'af_heart', 'af_sky', 'af_tessa', 'af_alloy', 'af_sarah',
        'am_daniel', 'am_jamie', 'am_matthew', 'am_mike', 'am_sam'
    ]
    
    selected_voice = st.selectbox(
        "Select Voice:",
        voice_options,
        index=0
    )
    
    # Audio settings
    st.subheader("Audio Settings")
    sample_rate = st.slider("Sample Rate", 16000, 48000, 24000, 1000)

# Generate audio button
if st.button("🎵 Generate Audio", type="primary"):
    if text_input.strip():
        with st.spinner("Generating audio..."):
            try:
                # Generate audio using pipeline
                audios = [audio for _, _, audio in st.session_state.pipeline(text_input, voice=selected_voice)]
                
                if audios:
                    # Combine all chunks
                    full_audio = np.concatenate(audios)
                    
                    # Create temporary file
                    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp_file:
                        sf.write(tmp_file.name, full_audio, sample_rate)
                        
                        # Display audio player
                        st.subheader("Generated Audio")
                        st.audio(tmp_file.name, format='audio/wav')
                        
                        # Audio info
                        duration = len(full_audio) / sample_rate
                        st.info(f"Audio duration: {duration:.2f} seconds")
                        
                        # Download button
                        with open(tmp_file.name, 'rb') as f:
                            st.download_button(
                                label="📥 Download Audio",
                                data=f.read(),
                                file_name=f"kokoro_tts_{selected_voice}.wav",
                                mime="audio/wav"
                            )
                        
                        # Clean up
                        os.unlink(tmp_file.name)
                        
                else:
                    st.error("No audio generated. Please check your input.")
                    
            except Exception as e:
                st.error(f"Error generating audio: {str(e)}")
    else:
        st.warning("Please enter some text to convert to speech.")

# Sidebar with information
with st.sidebar:
    st.header("About Kokoro TTS")
    st.markdown("""
    Kokoro is a text-to-speech model that can generate natural-sounding speech from text input.
    
    **Features:**
    - Multiple voice options
    - High-quality audio generation
    - Customizable sample rates
    
    **Voice Types:**
    - **af_**: Female voices
    - **am_**: Male voices
    """)
    
    st.header("Usage Tips")
    st.markdown("""
    1. Enter your text in the input area
    2. Select your preferred voice
    3. Adjust sample rate if needed
    4. Click 'Generate Audio'
    5. Play or download the result
    """)
    
    # Model status
    st.header("Model Status")
    if st.session_state.model_loaded:
        st.success("✅ Model loaded")
    else:
        st.error("❌ Model not loaded")

# Footer
st.markdown("---")
st.markdown("Built with Streamlit • Powered by Kokoro TTS")