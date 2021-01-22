"""test for the geo module"""

import floodsystem.geo
import floodsystem.station
import floodsystem.stationdata


def test_by_distance():
    """Test stations by distance function"""

    stations = floodsystem.stationdata.build_station_list()
    sorted_list = floodsystem.geo.stations_by_distance(stations, (0, 0))

    # check tuple entries are of expected types
    assert type(sorted_list[0][1]) == float
    assert type(sorted_list[0][0]) == floodsystem.station.MonitoringStation
    # check it is ordered correctly
    assert sorted_list[0][1] <= sorted_list[3][1]
    assert sorted_list[-1][1] >= sorted_list[0][1]
