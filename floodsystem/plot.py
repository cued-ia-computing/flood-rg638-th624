import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit
import matplotlib.dates as mdates


def plot_water_levels(station, dates, levels):
    """Given a station object and the corresponding lists of dates and water levels for that station,
    plots the water level against the dates, along with the typical high and low water levels for
    that station"""

    typical_high_list = []
    typical_low_list = []
    for i in range(len(dates)):
        typical_high_list.append(station.typical_range[1])
        typical_low_list.append(station.typical_range[0])

    plt.plot(dates, levels, 'crimson', label=f'Water level from {dates[-1]} until {dates[0]}')
    plt.plot(dates, typical_high_list, 'lawngreen', label='Typical high water level')
    plt.plot(dates, typical_low_list, 'indigo', label='Typical low water level')
    plt.xlabel("Time/Date")
    plt.ylabel("Water Level")
    plt.grid(True)
    plt.legend(loc="best")
    plt.tight_layout()
    plt.title(station.name)
    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    """Plots the water level against time, with the typical high, typical low and fitted polynomial of
    degree p also shown on the same plot"""

    poly, d0 = polyfit(dates, levels, p)
    poly_output = []
    for date in dates:
        poly_output.append(poly(mdates.date2num(date) - d0))
    plt.plot(dates, poly_output, 'cyan', label='Fitted Polynomial')
    plot_water_levels(station, dates, levels)
