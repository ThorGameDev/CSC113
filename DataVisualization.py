# November 17, 2023

import matplotlib.pyplot as plt

nov2021_tokyo_lows = [ 57,
              63,
              57,
              59,
              55,
              55,
              57,
              57,
              59,
              61,
              59,
              54,
              50,
              50,
              50,
              55,
              55,
              52,
              50,
              52,
              52,
              55,
              52,
              50,
              45,
              50,
              46,
              43,
              43,
              43]
nov2021_tokyo_highs = [ 68,
               70,
               70,
               66,
               66,
               64,
               66,
               68,
               68,
               70,
               70,
               68,
               63,
               68,
               64,
               64,
               63,
               63,
               63,
               64,
               59,
               66,
               61,
               61,
               66,
               59,
               57,
               59,
               54,
               63]
dates = []

for num in range(1,31):
    dates.append(f"Nov {num}")

fig, ax = plt.subplots()
ax.plot(dates, nov2021_tokyo_lows, linewidth=3, color='blue', label='Lows')
ax.plot(dates, nov2021_tokyo_highs, linewidth=3, color='red', label='Highs')

ax.set_title("Tokyo Weather highs and lows November 2021")
ax.set_xlabel("Date", fontsize=24)
ax.set_ylabel("Temperature in Fahrenheit")
ax.tick_params(axis='both', labelsize=8)

plt.xticks(rotation=90)
plt.show()
