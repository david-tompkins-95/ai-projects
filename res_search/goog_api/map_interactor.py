import requests as r

def makeReq():
    key = ""
    keyword = "Restaurants"
    radius = "50000"
    lat = 33.1983
    long = -96.614456
    res = r.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword={}&location={},{}&radius={}&key={}".format(keyword, lat, long, radius, key))
    print(res.text)

def test_speech():
    text = "test"
    return text

def _test(): 
    assert test_speech() == "test"

if __name__ == '__main__':
    _test()
