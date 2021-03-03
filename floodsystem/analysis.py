import numpy as np
import matplotlib.dates as dts


def polyfit(dates, levels, p):
    x = dts.date2num(dates)
    y = levels
    poly_coeff = np.polyfit(x - x[0], y, p)
    poly = np.poly1d(poly_coeff)
    d0 = x - x[0]
    return poly, d0
