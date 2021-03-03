import csv
import matplotlib.pyplot as plt
from datetime import datetime


# filename = 'data/sitka_weather_07-2018_simple.csv'
filename = 'data/death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    print(f"i  Column Name\n"
          f"-- -----------")
    for index, col_name in enumerate(header_row):
        print(f"{index}  {col_name}")

    dates = []
    highs = []
    lows = []
    for row in reader:
        try:
            cur_date = datetime.strptime(row[2], '%Y-%m-%d')
            my_high = int(row[4])
            my_low = int(row[5])
        except ValueError:
            print(f'Missing Data for *{row}*')
        else:
            dates.append(cur_date)
            highs.append(my_high)
            lows.append(my_low)
print(highs)

# Plot the high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')
ax.fill_between(dates, highs, lows, facecolor='green', alpha=0.2)

# format the plot
ax.set_title('Daily high & low temperatures, 2018', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
