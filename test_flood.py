from floodsystem.flood import stations_level_over_threshold
import floodsystem.stationdata


def test_stations_level_over_threshold():
    """Test stations level over threshold function"""

    stations = floodsystem.stationdata.build_station_list()
    test_list = stations_level_over_threshold(stations, 1)
    for i in range(len(test_list)):
        assert type(test_list[i][0]) == floodsystem.station.MonitoringStation
        assert type(test_list[i][1]) == float
    for i in range(len(test_list) - 1):
        assert test_list[i][1] >= test_list[i + 1][1]  # check its in descending order
