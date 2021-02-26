from floodsystem.station import MonitoringStation


def stations_level_over_threshold(stations, tol):
    """returns a list of tuples which hold a station where level is over tol and the relative level,
    sorted by the relative level in descending order"""

    threshold_list = []  # create empty list
    for s in stations:
        if type(MonitoringStation.relative_water_level(s)) == float:
            if MonitoringStation.relative_water_level(s) > tol and s.typical_range_consistent():
                water_level_tuple = (s, MonitoringStation.relative_water_level(s))  # create tuple
                threshold_list.append(water_level_tuple)  # append list with tuple if over threshold
    sorted_by_second = sorted(threshold_list, key=lambda tup: tup[1], reverse=True)
    return sorted_by_second


def stations_highest_rel_level(stations, N):
    """returns a list of the N stations (objects) at which the water level, relative to the typical range, is highest"""

    big_list = stations_level_over_threshold(stations, 0)  # creates a list of tuples of stations in descending order
    top_stations = []
    for i in range(N):
        top_stations.append(big_list[i][0])  # adds the station to the new list
    return top_stations
