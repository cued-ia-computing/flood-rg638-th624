from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
import datetime
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level, rate_of_water_rise
from floodsystem.analysis import polyfit


stations = build_station_list()
update_water_levels(stations)
top_5 = stations_highest_rel_level(stations, 5)

for station in top_5:
    dates, levels = fetch_measure_levels(station.measure_id, datetime.timedelta(days=2))
    plot_water_level_with_fit(station, dates, levels, 4)
    print(rate_of_water_rise(station))
