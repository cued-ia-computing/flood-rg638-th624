from floodsystem.stationdata import build_station_list
from floodsystem.geo import plot_stations_by_location
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_highest_rel_level


def run():
    """Requirements for Extension 1"""
    stations = build_station_list()
    update_water_levels(stations)

    # creating empty lists
    no_level_data = []
    below_typ_rng = []
    in_typ_rng = []
    above_typ_rng = []

    # separating station list into lists based on where the current water level is with respect to the typical range
    for station in stations:
        current_level = station.latest_level
        if station.typical_range is None:
            continue
        elif current_level is None:
            no_level_data.append(station)
        elif current_level < station.typical_range[0]:
            below_typ_rng.append(station)
        elif current_level < station.typical_range[1]:
            in_typ_rng.append(station)
        elif current_level > station.typical_range[1]:
            above_typ_rng.append(station)

    plot_stations_by_location(data1=in_typ_rng, data2=above_typ_rng, data3=below_typ_rng, data4=no_level_data,
                              label1='In typical range', label2='Above typical range', label3='Below typical range',
                              label4='No water level data')


if __name__ == "__main__":
    print("*** Extension Task Milestone 2: CUED Part IA Flood Warning System ***")
    run()
