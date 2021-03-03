import json

# Explore data structure
# filename = 'data/eq_data_1_day_m1.json'
filename2 = 'data/2020_07_16_30_day_earthquakes.json'
# readable_file = 'data/readable_eq_data.json'
readable_file2 = 'data/readable_eq_data2.json'

with open(filename2, encoding='utf-8') as f:
    all_eq_data = json.load(f)

with open(readable_file2, 'w', encoding='utf-8') as f:
    json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

mags = []
lons = []
lats = []

for eq_dicts in all_eq_dicts:
    mag = eq_dicts['properties']['mag']
    lon = eq_dicts['geometry']['coordinates'][0]
    lat = eq_dicts['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:10])
print(lats[:10])