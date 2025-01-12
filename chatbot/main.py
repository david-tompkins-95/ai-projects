import os
from chatbot.util.record_me import create_recording
from chatbot.util.res_play import playback
from chatbot.api.openai_api import get_speech
from chatbot.api.openai_api import gen_text

def main(): 
    print("Initializing Project...")
    # Get the root directory of the project
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    # Absolute path to chatbot/util/tmp
    tmp_dir = os.path.join(project_root, "chatbot", "util", "tmp")
    
    # Create the recording and save it to tmp_dir
    create_recording(tmp_dir)
    
    # Path to the text file that we want to read after creating the recording
    text_file_path = os.path.join(tmp_dir, "speech.txt")
    
    # Read the text from the file and generate AI Response
    try:
        with open(text_file_path, "r", encoding="utf-8") as file:
            text = file.read()
            gen_text(tmp_dir, text)

    except FileNotFoundError:
        print(f"Error: The file {text_file_path} was not found.")

    text_file_path = os.path.join(tmp_dir, "response.txt")

    try:
        with open(text_file_path, "r", encoding="utf-8") as file:
            text = file.read()
            get_speech(tmp_dir, text)

    except FileNotFoundError:
        print(f"Error: The file {text_file_path} was not found.")

    playback(tmp_dir)

    print("Project finished.")

if __name__ == '__main__':
    main()
