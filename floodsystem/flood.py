from floodsystem.station import MonitoringStation


def stations_level_over_threshold(stations, tol):
    list_of_tuples = []  # create empty list
    for s in stations:
        if type(MonitoringStation.relative_water_level(s)) == float:
            if MonitoringStation.relative_water_level(s) > tol:
                water_level_tuple = (s, MonitoringStation.relative_water_level(s))  # create tuple
                list_of_tuples.append(water_level_tuple)  # append list with tuple if over threshold
    return list_of_tuples
