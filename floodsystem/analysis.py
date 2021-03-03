import numpy as np
import matplotlib.dates as mdates
import datetime
from floodsystem.datafetcher import fetch_measure_levels


def polyfit(dates, levels, p):
    """Fits a polynomial of degree p to water level and datetime data"""
    x = mdates.date2num(dates)
    y = levels
    poly_coeff = np.polyfit(x - x[0], y, p)
    poly = np.poly1d(poly_coeff)
    d0 = x[0]
    return poly, d0


def find_average_water_level(station, days):
    """Finds the average water level at a specific station over the given last number of days,
     specified by the days parameter"""
    levels = fetch_measure_levels(station.measure_id, datetime.timedelta(days=days))[1]
    avg = np.mean(levels)
    return avg
