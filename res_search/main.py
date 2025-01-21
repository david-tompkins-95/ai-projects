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
from res_search.utils.data_control import create_csv

def main():
    key = ""
    keyword = "Bar"
    radius = "50000"
    lat =  29.749907
    long = -95.358421
    print("Making Request")
    # Get the root directory of the project
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    # Absolute path to chatbot/util/tmp
    tmp_dir = os.path.join(project_root, "res_search", "utils", "tmp")
    makeReq(tmp_dir, key, keyword, radius, lat, long)
    create_csv(tmp_dir)
    return 0

if __name__ == '__main__':
    main()
