from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1D"""
    station_list = build_station_list()
    print(stations_by_river(station_list))


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
