from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

station_list = build_station_list()
update_water_levels(station_list)

print(stations_level_over_threshold(station_list, 0.8))
