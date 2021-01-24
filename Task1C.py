from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1C"""

    stations = stations_within_radius(build_station_list(), [52.2053, 0.1218], 10)
    final_list = []
    for s in stations:
        name = s[0].station_id
        final_list.append(name)
    print(final_list.sort)


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
