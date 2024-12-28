# November 29, 2023
# Lab Downloading Data

# Exercise 16-2 Sitka, Death Valley Comparison
print("\nExercise 16-2 Sitka, Death Valley Comparison\n")

import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Get data about Sitka
filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = float(row[5])
        dates.append(current_date)
        highs.append(high)

# Get data about Death Valley
filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    d_dates, d_highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
        except:
            print(f"Missing data for {current_date}")
        else:
            d_dates.append(current_date)
            d_highs.append(high)

# Plot the graph
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(d_dates, d_highs, c='blue')
# Label and format the graph
ax.set_title("Sitaka-Death Valley comparison", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
