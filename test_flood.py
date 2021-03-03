import floodsystem.station
import floodsystem.stationdata
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level


def test_stations_level_over_threshold():
    """Test stations level over threshold function"""

    stations = floodsystem.stationdata.build_station_list()
    floodsystem.stationdata.update_water_levels(stations)
    test_list = stations_level_over_threshold(stations, 1)
    for i in range(len(test_list)):
        assert type(test_list[i][0]) == floodsystem.station.MonitoringStation
        assert type(test_list[i][1]) == float
    for i in range(len(test_list) - 1):
        assert test_list[i][1] >= test_list[i + 1][1]  # check its in descending order


def test_stations_highest_rel_level():
    """Test stations highest relative level function"""

    stations = floodsystem.stationdata.build_station_list()
    floodsystem.stationdata.update_water_levels(stations)
    test_list = stations_highest_rel_level(stations, 20)
    assert len(test_list) == 20
    for i in range(len(test_list)):
        assert type(test_list[i]) == floodsystem.station.MonitoringStation


def test_predict_future_level:
    """Test the predict future level function"""


