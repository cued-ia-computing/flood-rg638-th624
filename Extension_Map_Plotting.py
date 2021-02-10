from floodsystem.stationdata import build_station_list
from floodsystem.geo import plot_stations_by_location


def run():
    """Requirements for Extension 1"""
    stations = build_station_list()
    plot_stations_by_location(stations)


if __name__ == "__main__":
    print("*** Extension Task Milestone 1: CUED Part IA Flood Warning System ***")
    run()
