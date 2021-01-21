"""test for the geo module"""

import floodsystem.stationdata
import floodsystem.geo

def test_by_distance():
    """Test stations by distance"""

    stations = floodsystem.stationdata.build_stations_list  # build stations list
    sorted_list = floodsystem.geo.stations_by_distance(stations, (52.2053, 0.1218))
