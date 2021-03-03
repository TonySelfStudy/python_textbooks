import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
from plotly import colors

# Extract key earthquake info from json file
# filename = 'data/eq_data_30_day_m1.json'
# filename = 'data/2020_07_16_30_day_earthquakes.json'
filename = 'data/readable_eq_data2.json'

with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []

for eq_dicts in all_eq_dicts:
    mag = eq_dicts['properties']['mag']
    lon = eq_dicts['geometry']['coordinates'][0]
    lat = eq_dicts['geometry']['coordinates'][1]
    title = eq_dicts['properties']['title']
    if mag is not None:
        if mag > 0:
            mags.append(mag)
            lons.append(lon)
            lats.append(lat)
            hover_texts.append(title)

# Map the earthquakes

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [mag*3 for mag in mags],
        'color': mags,
        'reversescale': True,
        'colorscale': 'Hot',
        'colorbar': {'title': 'Magnitude'},
    },
}]

my_layout = Layout(title={
    'text': "Global earthquakes in the last month",
    'y': 0.9,
    'x': 0.5,
    'xanchor': 'center',
    'yanchor': 'top'})

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename=f'kaiju_detected.html')

