### This project is built using Python 3 and the Google Maps API
# Objective: Find nearby Restaurant Information
# Convert Data to simple csv file
# Built By David M. Tompkins. 

import os
from res_search.config import config
from res_search.goog_api.map_interactor import makeReq
from res_search.utils.data_control import create_csv

def main():
    print("Making Request")
    # Get the root directory of the project
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    # Absolute path to chatbot/util/tmp
    tmp_dir = os.path.join(project_root, "res_search", "utils", "tmp")
    # Convert Env Variable to list
    cities_str = config.CITIES
    CITIES = cities_str.split(',')
    for city in CITIES:
        print(city)
        if(city == "McKinney"):
            makeReq(tmp_dir, config.API_KEY, config.KEYWORD, config.RADIUS, config.LAT_MCKINNEY, config.LONG_MCKINNEY)
        elif(city == "Celina"):
            makeReq(tmp_dir, config.API_KEY, config.KEYWORD, config.RADIUS, config.LAT_CELINA, config.LONG_CELINA)
        elif(city == "Frisco"):
            makeReq(tmp_dir, config.API_KEY, config.KEYWORD, config.RADIUS, config.LAT_FRISCO, config.LONG_FRISCO)  
        elif(city == "Little Elm"):
            makeReq(tmp_dir, config.API_KEY, config.KEYWORD, config.RADIUS, config.LAT_LELM, config.LONG_LELM)   
        create_csv(tmp_dir, city)
    return 0

if __name__ == '__main__':
    main()
