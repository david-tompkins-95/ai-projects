import sounddevice as sd
from scipy.io.wavfile import write
from chatbot.util.transcripe_speech import transcribe
import os
import numpy as np

def create_recording(directory):
    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)
    print(f"Directory ensured: {directory}")

    # Define file paths
    filename = "speech.wav"
    filepath = os.path.join(directory, filename)

    # Sampling parameters
    fs = 44100  # Sampling frequency
    seconds = 5  # Recording duration

    try:
        print("Starting recording...")
        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()  # Wait for recording to complete
        print("Recording complete!")

        # Convert to int16 for saving
        int_recording = np.int16(recording * 32767)

        # Save the recording
        print(f"Saving recording...")
        write(filepath, fs, int_recording)
        print(f"Recording saved successfully!")

        # Transcribe the audio file
        transcribe(filepath)

    except Exception as e:
        print(f"An error occurred: {e}")
