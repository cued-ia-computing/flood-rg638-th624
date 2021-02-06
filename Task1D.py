from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1D"""
    station_list = build_station_list()
    print(rivers_with_station(station_list))


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
