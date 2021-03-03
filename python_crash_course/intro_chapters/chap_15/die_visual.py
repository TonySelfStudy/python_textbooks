from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

NUM_DICE = 2
NUM_SIDES_1 = 6
NUM_SIDES_2 = 6
NUM_ROLLS = 100000

# Create D*'s
die1 = Die(NUM_SIDES_1)
die2 = Die(NUM_SIDES_2)

max_roll = die1.num_sides * die2.num_sides

# Roll the bones
results = []
for rolls in range(NUM_ROLLS):
    result = die1.roll() * die2.roll()
    results.append(result)

print(f"Number of rolls = {NUM_ROLLS}")
if NUM_ROLLS < 200:
    print(results)

# Analyze roll results
frequencies = []
x_values = list(range(1, max_roll + 1))
for val in x_values:
    count = results.count(val)
    frequencies.append(count)
    print(f"A roll of {val} occurred: {count} times or {(count/NUM_ROLLS*100):5.2f}%")

# Plot in plotly
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': 'Roll Value', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Roll'}
my_layout = Layout(title=f'Result of rolling a D{NUM_SIDES_1} * D{NUM_SIDES_2} '
                         f'{NUM_ROLLS} times',
                   xaxis=x_axis_config,
                   yaxis=y_axis_config,)
offline.plot({'data': data,
              'layout': my_layout},
             filename='2d6.html'
             )
