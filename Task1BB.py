from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1B"""

    stations = build_station_list()  # Builds list of stations

    stations_by_distance(stations, (52.2053, 0.1218))  # implement demonstration program


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IB Flood Warning System ***")
    run()
