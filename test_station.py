# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list


def test_create_monitoring_station():
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


def test_inconsistent_typical_range():
    """Tests the inconsistent typical range function"""

    stations = build_station_list()
    test_list = inconsistent_typical_range_stations(stations)

    # Checks that typical range data for any station object in the produced list is either unavailable or inconsistent
    for station in test_list:
        assert station.typical_range is None or station.typical_range[0] > station.typical_range[1]


def test_relative_water_level():
    """Tests the relative water level function"""

    test_list = inconsistent_typical_range_stations(build_station_list())
    for station in test_list:
        assert MonitoringStation.relative_water_level(station) is None
        if station.latest_level is None:
            assert MonitoringStation.relative_water_level(station) is None
