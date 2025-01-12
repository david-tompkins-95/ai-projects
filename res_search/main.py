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
from res_search.goog_api.map_interactor import makeReq

def main():
    print("Making Request")
    makeReq()
    create_csv()
    return 0

if __name__ == '__main__':
    main()
