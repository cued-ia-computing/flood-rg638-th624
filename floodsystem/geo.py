# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from bokeh.tile_providers import get_provider, Vendors
from haversine import haversine  # for calculating distance between points
from .utils import sorted_by_key  # noqa
from bokeh.plotting import figure, output_file, show
from converter import lat2y, lon2x


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
    stations_list = stations_by_distance(stations, centre)  # create list of tuples using previous function
    for s in stations_list:  # iterate through
        if s[1] <= r:
            list_of_stations.append(s)  # add any stations within the radius to the empty list
    return list_of_stations  # return this list


def rivers_with_station(stations):
    """Takes a list of stations and returns a set of the names of the rivers"""

    set_of_rivers = set()  # create set (to avoid duplicates)
    for s in stations:
        set_of_rivers.add(s.river)  # add rivers to set
    return sorted(set_of_rivers)  # turns set back to list


def stations_by_river(stations):
    """Takes a list of stations and returns a dictionary that maps river names to a list of stations on a given river"""

    river_dict = {}
    for n in rivers_with_station(stations):
        river_stations = []
        for m in stations:
            if m.river == n:
                river_stations.append(m.name)
        river_dict[n] = river_stations
    return river_dict


def rivers_by_station_number(stations, N):
    """ Returns a list of tuples containing the name of a river and number of monitoring stations on that river for the
    N rivers with the greatest amount of monitoring stations, sorted in decreasing order of number of stations """

    rivers_with_number = []
    for river in rivers_with_station(stations):  # Iterates through the full list of rivers with a monitoring station
        station_counter = 0
        for monitoring_station in stations:
            if monitoring_station.river == river:
                station_counter += 1  # Iterates through full station list and counts number of times each river appears
        rivers_with_number.append((river, station_counter))
    complete_list = sorted_by_key(rivers_with_number, 1)
    complete_list.reverse()
    shortened_list = complete_list[:N]

    # If the station_counter value for the (N+i)th term in the list is the same as the value for the Nth term
    # It will also be included in the list

    for i in range(len(complete_list) - N):
        # The Nth term in the list is given by the (N-1)th index
        if complete_list[N-1][1] == complete_list[N + i][1]:
            shortened_list.append(complete_list[N+i])
        # The for loop is broken early once the (N+i)th station value is no longer equal to the Nth value
        elif complete_list[N-1][1] != complete_list[N + i][1]:
            break

    return shortened_list


def plot_stations_by_location(data1, colour1='palegoldenrod', data2=None, colour2='fuchsia', data3=None,
                              colour3='lime', data4=None, colour4='cyan', label1='undefined1',
                              label2='undefined2', label3='undefined3', label4='undefined4'):
    """Plots the locations of floodstations as points on a map"""
    p = figure(x_range=(-1100000, 300000), y_range=(6300000, 8200000),
               x_axis_type="mercator", y_axis_type="mercator")
    output_file("tile.html")
    tile_provider = get_provider(Vendors.CARTODBPOSITRON)
    p.add_tile(tile_provider)

    x1 = []
    y1 = []

    for a in data1:
        x1.append(lon2x(a.coord[1]))
        y1.append(lat2y(a.coord[0]))

    p.circle_dot(x1, y1, color=colour1, legend_label=label1)

    if data2 is not None:
        x2 = []
        y2 = []
        for b in data2:
            x2.append(lon2x(b.coord[1]))
            y2.append(lat2y(b.coord[0]))
        p.circle_dot(x2, y2, color=colour2, legend_label=label2)

    if data3 is not None:
        x3 = []
        y3 = []
        for c in data3:
            x3.append(lon2x(c.coord[1]))
            y3.append(lat2y(c.coord[0]))
        p.circle_dot(x3, y3, color=colour3, legend_label=label3)

    if data4 is not None:
        x4 = []
        y4 = []
        for d in data4:
            x4.append(lon2x(d.coord[1]))
            y4.append(lat2y(d.coord[0]))
        p.circle_dot(x4, y4, color=colour4, legend_label=label4)

    show(p)




