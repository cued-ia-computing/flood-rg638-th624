from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()

    print(stations_by_distance(stations, [52.2053, 0.1218]))


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IB Flood Warning System ***")
    run()
