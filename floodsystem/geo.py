# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from haversine import haversine  # for calculating distance between points

from .utils import sorted_by_key  # noqa


def stations_by_distance(stations, p):
    """Takes a list stations and creates a list of tuples including the station and
     it's distance from a point, then sorts this list in order of distance"""

    distance_list = []  # create empty list
    for s in stations:  # iterate through list of stations
        distance = haversine(s.coord, p)  # calculate distance
        distance_tuple = (s, distance)  # create tuple
        distance_list.append(distance_tuple)  # add tuple to list
    return sorted_by_key(distance_list, 1)  # returns a list sorted by distance


def stations_within_radius(stations, centre, r):
    """Takes a list of stations and returns a list of the stations within
    a radius of a coordinate"""

    list_of_stations = []  # create empty list
    stations_list = stations_by_distance(stations, centre) # create list of tuples using previous function
    for s in stations_list:  # iterate through
        if s[1] <= r:
            list_of_stations.append(s)  # add any stations within the radius to the empty list
    return list_of_stations  # return this list
