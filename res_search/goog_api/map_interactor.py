import requests as r
import os
import json

def makeReq(tmp_dir, key, keyword, radius, lat, long):
    # Ensure the directory exists
    os.makedirs(tmp_dir, exist_ok=True)
    # Create filepath
    filename_json = "res.json"
    filepath_json = os.path.join(tmp_dir, filename_json)
    # Make request for google apis
    res = r.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword={}&location={},{}&radius={}&key={}".format(keyword, lat, long, radius, key))
    # Write JSON to file
    res = json.loads(res.text)
    if 'results' in res:
        res = res['results']
    # Create a list to hold the filtered results
    filtered_res = []
    # Loop through each object in the list to extract required fields
    for item in res:
        filtered_item = {key: item[key] for key in ['business_status', 'name', 'price_level', 'rating', 'user_ratings_total'] if key in item}
        filtered_res.append(filtered_item)

    # Convert the filtered list back to JSON
    res_json = json.dumps(filtered_res, ensure_ascii=False)
    # Writing to the file
    with open(filepath_json, "w", encoding="utf-8") as text_file:
        text_file.write(res_json)

    print("File Written")

def test_speech():
    text = "test"
    return text

def _test(): 
    assert test_speech() == "test"

if __name__ == '__main__':
    _test()
