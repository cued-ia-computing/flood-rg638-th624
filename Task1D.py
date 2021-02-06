from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1D"""
    station_list = build_station_list()
    print("number of rivers: ")
    print(len(rivers_with_station(station_list)))  # prints length of list of rivers
    print("first 10 rivers alphabetically: ")
    print(rivers_with_station(station_list)[:10])  # prints first 10 items in list (list is already sorted)
    print("stations on River Aire: ")
    print(sorted(stations_by_river(station_list)["River Aire"]))
    print("stations on River Cam: ")
    print(sorted(stations_by_river(station_list)["River Cam"]))
    print("stations on River Thames: ")
    print(sorted(stations_by_river(station_list)["River Thames"]))


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
