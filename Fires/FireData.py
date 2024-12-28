# November 30, 2023

# Pandas is used for reading and accessing the CSV file
import pandas as pd
# Used for plotting the graph
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Load the fire data
fire_data = pd.read_csv('viirs-snpp_2021_United_States.csv')

# Extracts the latitude and longitude of each fire to be graphed
lat, lon = [], []
for item in fire_data.loc[:,'longitude']:
    lon.append(float(item))
for item in fire_data.loc[:,'latitude']:
    lat.append(float(item))

# Trims the data set to be rendered within a human lifetime
lat = lat[:200]
lon = lon[:200]

# Prepares data for plotly
data = [{
    'type': 'scattergeo',
    'lon': lon,
    'lat': lat,
}]

# Plots the graph
my_layout = Layout(title='2021 United states Fires')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='Fires.html')
