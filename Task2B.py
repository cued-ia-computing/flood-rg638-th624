from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

station_list = build_station_list()
update_water_levels(station_list)

list_of_tuples = stations_level_over_threshold(station_list, 0.8)

for i in range(len(list_of_tuples)):  # cycle through tuples
    print((list_of_tuples[i][0]).name, list_of_tuples[i][1])  # prints name and relative water level
