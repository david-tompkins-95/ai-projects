import os
import speech_recognition as sr

def transcribe(filepath_wav):
    print(f"Transcribing file...")

    try:
        # Initialize recognizer
        r = sr.Recognizer()
        with sr.AudioFile(filepath_wav) as source:
            audio = r.record(source)

        # Perform transcription
        text = r.recognize_google(audio)
        print("Transcription:", text)

        # Save transcription
        directory = os.path.dirname(filepath_wav)
        filepath_txt = os.path.join(directory, "speech.txt")
        with open(filepath_txt, "w") as f:
            f.write(text)
        print(f"Transcription saved!")

    except FileNotFoundError:
        print(f"Error: WAV file not found at {filepath_wav}")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google's servers. Error: {e}")
    except Exception as e:
        print(f"An error occurred during transcription: {e}")
