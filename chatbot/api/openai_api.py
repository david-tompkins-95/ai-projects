from pathlib import Path 
from openai import OpenAI
import os

client = OpenAI()

def gen_text(directory, text):
    print("Generating response...")
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system", 
                "content": "You are a fun assistant that gives really short but funny answers and can talk back to me when you feel like im asking a controversial question."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    # Extract the generated response
    generated_text = completion.choices[0].message.content
    
    # Define the text file path
    filename_text = "response.txt"
    filepath_text = os.path.join(directory, filename_text)

    # Write the generated text to a file
    with open(filepath_text, "w", encoding="utf-8") as text_file:
        text_file.write(generated_text)
    
    print(f"Response saved!")

def get_speech(directory, text):
    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)
    print(f"Directory ensured: {directory}")

    # Define file paths
    filename = "speech.mp3"
    filepath = os.path.join(directory, filename)

    print("Getting OpenAI speech...")
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input = text
    )

    # Save the response content to a file
    with open(filepath, "wb") as audio_file:
        audio_file.write(response.content)  # Write the binary content to the file

    print(f"AI is Finished!")

def test_speech():
    text = "test"
    return text

def _test(): 
    assert test_speech() == "test"

if __name__ == '__main__':
    _test()
