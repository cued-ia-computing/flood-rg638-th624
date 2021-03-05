import math


def lat2y(a):
    """ Converts latitude co-ordinate to its web mercator equivalent """
    radius = 6378137.0  # in meters on the equator
    return math.log(math.tan(math.pi / 4 + math.radians(a) / 2)) * radius


def lon2x(a):
    """ Converts longitudinal co-ordinate to its web mercator equivalent"""
    radius = 6378137.0  # in meters on the equator
    return math.radians(a) * radius
