import sounddevice as sd
from pydub import AudioSegment
import soundfile as sf 
import os

def playback(directory):
    # Convert the mp3 to WAV and then proceed to playback
    mp3_file_path = os.path.join(directory, "speech.mp3")
    output_path = os.path.join(directory, "response.wav")
    sound = AudioSegment.from_mp3(mp3_file_path)
    # Convert to WAV
    sound.export(output_path, format="wav")
    # Read the WAV file
    data, fs = sf.read(output_path, dtype='float32')

    # Play the audio
    print("Playing Audio...")
    sd.play(data, fs)
    # Wait for playback to finish
    sd.wait()
    print("Playback Complete!")
