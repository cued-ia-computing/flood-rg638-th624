import matplotlib.pyplot as plt


def plot_water_levels(station, dates, levels):
    """Given a station object and the corresponding lists of dates and water levels for that station,
    plots the water level against the dates, along with the typical high and low water levels for
    that station"""
    typical_high_list = []
    typical_low_list = []
    for i in range(len(dates)):
        typical_high_list.append(station.typical_range[1])
        typical_low_list.append(station.typical_range[0])

    plt.plot(dates, levels, 'r', label=f'Water level from {dates[-1]} until {dates[0]}')
    plt.plot(dates, typical_high_list, 'b', label='Typical high water level')
    plt.plot(dates, typical_low_list, 'm', label='Typical low water level')
    plt.xlabel("Date")
    plt.ylabel("Water Level")
    plt.grid(True)
    plt.legend(loc="best")
    plt.tight_layout()
    plt.title(station.name)
    plt.show()
