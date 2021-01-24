from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1C"""

    close_stations = stations_within_radius(build_station_list(), [52.2053, 0.1218], 10)
    final_list = []
    for s in close_stations:
        final_list.append(s[0].name)
    print(sorted(final_list))


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
