import floodsystem.geo

def test_by_distance():
    stations = build_stations_list  #  build stations list
    sorted_list = stations_by_distance(stations, (52.2053, 0.1218))
