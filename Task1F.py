from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations


def run():
    """Requirements for Task 1F"""
    stations = build_station_list()
    inconsistent_station_objects = inconsistent_typical_range_stations(stations)
    inconsistent_station_names = []
    for station in inconsistent_station_objects:
        inconsistent_station_names.append(station.name)  # Maps name for each station object to a new list of only names
    inconsistent_station_names.sort()
    print(inconsistent_station_names)


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
