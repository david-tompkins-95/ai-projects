import requests as r
import os
import json
### Data Needed
# business_status
# name
# opening_hours.open_now
# price_level
# rating
# user_ratings_total

def makeReq(tmp_dir, key, keyword, radius, lat, long):
    # Ensure the directory exists
    os.makedirs(tmp_dir, exist_ok=True)
    # Create filepath
    filename_json = "res.json"
    filepath_json = os.path.join(tmp_dir, filename_json)
    # Make request for google apis
    res = r.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword={}&location={},{}&radius={}&key={}".format(keyword, lat, long, radius, key))
    # Write JSON to file
    # res = json.loads(res.text)
    with open(filepath_json, "w", encoding="utf-8") as text_file:
        text_file.write(res.text)
    print("File Written")

def test_speech():
    text = "test"
    return text

def _test(): 
    assert test_speech() == "test"

if __name__ == '__main__':
    _test()
