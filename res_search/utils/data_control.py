import pandas as pd
import os

def create_csv(tmp_dir):
    # Assuming 'res.json' is your JSON file
    # Define file paths
    filename = "res.json"
    filename_csv = "output.csv"
    filepath = os.path.join(tmp_dir, filename)
    data = pd.read_json(filepath)
    data.to_csv(os.path.join(tmp_dir, filename_csv), index=False)
    return 0

def test_speech():
    text = "test"
    return text

def _test(): 
    assert test_speech() == "test"

if __name__ == '__main__':
    _test()