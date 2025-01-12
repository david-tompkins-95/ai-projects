### This project is built using Python 3 and the Google Maps API
# Objective: Find nearby Restaurant Information
# - Hours
# - Peak Hours
# - Phone Number
# - Address
# - Food Type
# - Google Stars
# Cities: McKinney, Prosper, Selina, Frisco, Little Elm
# Convert Data to simple csv file
# Built By David M. Tompkins. 
import os
from res_search.goog_api.map_interactor import makeReq

def main():
    key = "AIzaSyBwF8CSFpQUQBtnk7hNNQlx38eFw6836Rk"
    keyword = "Restaurants"
    radius = "50000"
    lat = 33.1983
    long = -96.614456
    print("Making Request")
    # Get the root directory of the project
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    # Absolute path to chatbot/util/tmp
    tmp_dir = os.path.join(project_root, "res_search", "utils", "tmp")
    makeReq(tmp_dir, key, keyword, radius, lat, long)
    # create_csv()
    return 0

if __name__ == '__main__':
    main()
