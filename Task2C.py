import floodsystem.station
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    stations = build_station_list()
    update_water_levels(stations)

    list_of_stations = stations_highest_rel_level(stations, 10)
    for i in range(len(list_of_stations)):
        print(list_of_stations[i].name, floodsystem.station.MonitoringStation.relative_water_level(list_of_stations[i]))


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
