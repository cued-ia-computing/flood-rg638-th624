"""test for the geo module"""

import floodsystem.geo
import floodsystem.station
import floodsystem.stationdata


def test_stations_by_distance():
    """Test stations by distance function"""

    stations = floodsystem.stationdata.build_station_list()
    sorted_list = floodsystem.geo.stations_by_distance(stations, (0, 0))

    # check tuple entries are of expected types
    for n in sorted_list:
        assert type(n[1]) == float
        assert type(n[0]) == floodsystem.station.MonitoringStation
    # check it is ordered correctly
    for n in range(len(sorted_list) - 1):
        assert sorted_list[n][1] <= sorted_list[n + 1][1]


def test_stations_within_radius():
    """Test stations within radius function"""

    stations = floodsystem.stationdata.build_station_list()
    new_list = floodsystem.geo.stations_within_radius(stations, [52.2053, 0.1218], 10)

    for n in new_list:
        # check tuple entries are of expected types
        assert type(n[0]) == floodsystem.station.MonitoringStation
        assert type(n[1]) == float
        # check they are actually within radius
        assert n[1] <= 10

def test_rivers_with_station():
    """Test rivers with station function"""

    stations = floodsystem.stationdata.build_station_list()
    river_set = floodsystem.geo.rivers_with_station(stations)

    assert type(river_set) == set  # check a set is returned
    for n in river_set:
        assert type(n) == str  # check it's full of strings
        for m in river_set:
            assert n != m  # check for duplicates

