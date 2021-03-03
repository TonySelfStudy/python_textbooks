# Generalize the exampls from Chapter 16 to plot multiple datasets
import csv
import matplotlib.pyplot as plt
from datetime import datetime


def plot_station(file_name, date_format='%Y-%m-%d', ax = None, fig = None,
                 low_color = 'blue', high_color = 'red', shade_color = 'green'):
    """Plot temperature min and max for a weather station.

    Parameters
    ----------
    file_name - str
        File containing meteorological (MET) csv data
    date_format - str
        Parsing string to convert time stamp to datetime object
    ax - Axes
        Axis to plot data to, if None a new axis is created
    fig - Figure
        Figure to plot data to, if ax is None a new Figure is created

    Returns
    -------
    station_name - str
        NOAA met station name
    dates - datetime
        Date/time for MET measurement
    highs - integer list
        Daily high temperature
    lows - integer list
        Daily low temperature
    Notes
    -------
    """

    station_name = None
    dates = []
    highs = []
    lows = []

    # Index locations of desired data
    i_name = None
    i_date = None
    i_tmax = None
    i_tmin = None

    # Read in MET data
    with open(file_name) as f:
        reader = csv.reader(f)

        # Read in the header row and find the column index
        # for Station name, date, and temperature information
        header_row = next(reader)
        # print(header_row)

        print(f"i  Column Name\n"
              f"-- -----------")
        for index, col_name in enumerate(header_row):
            print(f"{index}  {col_name}")
            if col_name == "NAME":
                i_name = index
            if col_name == "DATE":
                i_date = index
            if col_name == "TMAX":
                i_tmax = index
            if col_name == "TMIN":
                i_tmin = index

        # Read the remaining rows of data
        for row in reader:
            try:
                cur_date = datetime.strptime(row[i_date], date_format)
                my_high = int(row[i_tmax])
                my_low = int(row[i_tmin])
            except ValueError:
                print(f'Missing Data for *{row}*')
            else:
                dates.append(cur_date)
                highs.append(my_high)
                lows.append(my_low)
        station_name = row[i_name]
    # print(highs)

    # Plot the high temperatures
    if ax is None:
        fig, ax = plt.subplots()

    plt.style.use('seaborn')
    ax.plot(dates, highs, c=high_color, label=f'{station_name} High')
    ax.plot(dates, lows, c=low_color, label=f'{station_name} Low')
    ax.fill_between(dates, highs, lows, facecolor=shade_color, alpha=0.2)

    # format the plot
    ax.set_title(f'Daily high & low temperatures', fontsize=20)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel('Temperature (F)', fontsize=16)
    ax.set_ylim([20, 140])
    ax.tick_params(axis='both', which='major', labelsize=16)
    ax.legend()

    return station_name, dates, highs, lows

if __name__ == '__main__':

    file_name1 = 'data/sitka_weather_2018_simple.csv'
    file_name2 = 'data/death_valley_2018_simple.csv'
    file_name3 = 'data/NOAA Weather SFO.csv'
    file_name4 = 'data/NOAA Weather SMF.csv'

    fig1, ax1 = plt.subplots()
    plot_station(file_name1, ax=ax1, fig=fig1)
    plot_station(file_name2, ax=ax1, fig=fig1, low_color='cyan', high_color='orange', shade_color='grey')

    fig2, ax2 = plt.subplots()
    plot_station(file_name3, ax=ax2, fig=fig2)
    plot_station(file_name4, ax=ax2, fig=fig2, low_color='cyan', high_color='orange', shade_color='grey')

    plt.show()

