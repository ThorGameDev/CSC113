# November 28, 2023

# Import necessary libraries
# Pandas is used for extracting data from the csv file
import pandas as pd
# Matplotlib is used for displaying the data
import matplotlib.pyplot as plt

# Reads the csv file and saves it to a variable
river_data = pd.read_csv("nile.csv")

# Extracts the year and flood columns from river_data
Years : pd.Series = river_data.iloc[:, 0]
Flood : pd.Series = river_data.iloc[:, 1]

# Displays relevant information
print(f"Number of records is {len(Years)}")
print(f"Average height is {Flood.mean()}")
print(f"Maximum height is {Flood.min()}")
print(f"Maximum height is {Flood.max()}")
print(f"Recommended height is {Flood.quantile(0.95)} or above, because floods this high are rare")

# Sets the tool pandas uses for plotting
pd.options.plotting.backend = 'matplotlib'
# Plots flood data
Flood.plot()

# Displays the Matplotlib graph
plt.show()
