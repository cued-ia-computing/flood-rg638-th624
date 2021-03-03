import numpy as np
import matplotlib.dates as mdates


def polyfit(dates, levels, p):
    """Fits a polynomial of degree p to water level and datetime data"""

    x = mdates.date2num(dates)
    y = levels
    poly_coeff = np.polyfit(x - x[-1], y, p)
    poly = np.poly1d(poly_coeff)
    d0 = x[-1]
    return poly, d0
