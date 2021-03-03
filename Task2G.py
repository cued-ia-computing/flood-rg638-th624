from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level, rate_of_water_rise, predict_future_level
from floodsystem.station import MonitoringStation


def run():
    """In order to determine the risk at each station I took into account both the current relative water level
    and the rate of change of the water level. I calculated the derivative of the polynomial for the
    final datapoint, which allowed the instantaneous current rate of change to be extrapolated linearly to predict
    the water level in two days. This was converted to a 'relative' level and was combined with the current relative
    water level (the current level was weighted slightly more heavily) to produce a quantitative risk value.
    This quantitative value was then used to class the flood-risk at each station categorically."""

    # create a list of the top 50 stations with the highest current level as classing all stations takes too long
    stations = build_station_list()
    update_water_levels(stations)
    top_50 = stations_highest_rel_level(stations, 50)

    # initialise final list
    final_list = []

    for station in top_50:
        current_level = station.latest_level
        current_instantaneous_change = rate_of_water_rise(station)
        current_relative_level = MonitoringStation.relative_water_level(station)

        # ignore stations for which the instantaneous change can not be calculated
        if current_instantaneous_change is None:
            continue

        # provides a default value for stations with unreliable current instantaneous change values
        if abs((current_instantaneous_change / current_level)) > 0.5:
            predicted_level = current_level

        else:
            predicted_level = predict_future_level(station, 2)  # predicts future level

        predicted_relative_level = (predicted_level - station.typical_range[0]) / \
                                   (station.typical_range[1] - station.typical_range[0])

        quantitative_risk = (predicted_relative_level * 0.4 + current_relative_level * 0.6)

        if quantitative_risk > 1.25:
            risk_factor = 'severe'

        elif quantitative_risk > 1:
            risk_factor = 'high'

        elif quantitative_risk > 0.75:
            risk_factor = 'moderate'

        else:
            risk_factor = 'low'

        final_list.append([station.name, risk_factor, quantitative_risk])

    # the list is sorted in decreasing order of quantitative risk
    final_list.sort(key=lambda x: x[2])
    final_list.reverse()

    # removes the quantitative risk value from the list so it is not displayed in the output
    for station in final_list:
        station.pop(2)

    print('Flood stations at highest risk:')
    for i in final_list:
        print(f'Station: {i[0]}, Risk Level: {i[1]}')


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
