from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_num_of_stations


def run():
    """Requirements for Task 1E"""

    stations = build_station_list()
    final_list = rivers_by_num_of_stations(stations, 9)
    print(final_list)


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()