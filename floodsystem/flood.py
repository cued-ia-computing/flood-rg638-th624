from floodsystem.station import MonitoringStation
from floodsystem.stationdata import update_water_levels

def stations_level_over_threshold(stations, tol):
    update_water_levels(stations)
    list_of_tuples = []
    for s in stations:
        if type(MonitoringStation.relative_water_level(s)) == float:
            if MonitoringStation.relative_water_level(s) > tol:
                water_level_tuple = (s, MonitoringStation.relative_water_level(s))  # create tuple
                list_of_tuples.append(water_level_tuple)  # append list with tuple if over threshold
    return list_of_tuples
