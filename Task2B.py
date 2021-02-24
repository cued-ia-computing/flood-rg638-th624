from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold

station_list = build_station_list()

print(stations_level_over_threshold(station_list, 0.8))
