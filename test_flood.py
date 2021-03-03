import floodsystem.station
import floodsystem.stationdata
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level, \
    predict_future_level, rate_of_water_rise
import random


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


def test_predict_future_level():
    """Test the predict future level function"""

    stations = floodsystem.stationdata.build_station_list()
    floodsystem.stationdata.update_water_levels(stations)
    for i in range(5):
        station = stations[random.randint(1, 1000)]  # selects random floodstation
        if rate_of_water_rise(station) is None:
            continue

        # if the rate of change is positive then the future level should be greater than the current level
        elif rate_of_water_rise(station) > 0:
            assert(predict_future_level(station, 5) > station.latest_level)

        # if the rate of change is negative then the future level should be greater than the current level
        elif rate_of_water_rise(station) < 0:
            assert(predict_future_level(station, 5) < station.latest_level)

        else:
            continue
