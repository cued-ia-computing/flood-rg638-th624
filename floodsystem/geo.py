# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from haversine import haversine  # for calculating distance between points

from .utils import sorted_by_key  # noqa


def stations_by_distance(stations, p):
    distance_list = []  # create empty list
    for s in stations:  # iterate through list of stations
        distance = haversine(s.coord, p)  # calculate distance
        distance_tuple = (s, distance)  # create tuple
        distance_list.append(distance_tuple)  # add tuple to list
    return sorted_by_key(distance_list, 1)  # returns a list sorted by distance
