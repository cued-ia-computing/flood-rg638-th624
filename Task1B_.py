from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


#  This is named Task1B_ rather than Task1B as pycharm was not detecting my file as a python file with the old name
#  Have changed the reference for the file in .github/workflows/pythonapp.yml to Task1B_ to account for this

def run():
    """Requirements for Task 1B"""

    stations = build_station_list()  # Builds list of stations

    # implement demonstration program
    list = stations_by_distance(stations, (52.2053, 0.1218))
    print(list[:10])
    print(list[-10:])


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
