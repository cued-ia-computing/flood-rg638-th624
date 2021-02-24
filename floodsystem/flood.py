from floodsystem.station import MonitoringStation


def stations_level_over_threshold(stations, tol):
    threshold_list = []  # create empty list
    for s in stations:
        if type(MonitoringStation.relative_water_level(s)) == float:
            if MonitoringStation.relative_water_level(s) > tol and s.typical_range_consistent():
                water_level_tuple = (s, MonitoringStation.relative_water_level(s))  # create tuple
                threshold_list.append(water_level_tuple)  # append list with tuple if over threshold
    sorted_by_second = sorted(threshold_list, key=lambda tup: tup[1], reverse=True)
    return sorted_by_second
