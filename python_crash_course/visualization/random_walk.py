import matplotlib.pyplot as plt
from random import choice
from tony_functions import *

print_header('Chapter 15, Starting Page = 316')


class RandomWalk:
    """Random Walk Analysis"""

    def __init__(self):
        self.max_steps = 50_000
        self.max_x_step = 5
        self.max_y_step = 5
        self.x_vals = [0]
        self.y_vals = [0]
        self.start_walk()
        print(f'walking complete')

    def start_walk(self):
        while len(self.x_vals) < self.max_steps:
            x_step, y_step = self.single_step()
            if not (x_step == 0 and y_step == 0):
                x = self.x_vals[-1]
                y = self.y_vals[-1]
                self.x_vals.append(x_step+x)
                self.y_vals.append(y_step+y)

    def single_step(self):
        x_direction = choice([-1, 1])
        y_direction = choice([-1, 1])
        x_distance = choice(range(5))
        y_distance = choice(range(5))
        x_step = x_direction * x_distance
        y_step = y_direction * y_distance
        return x_step, y_step


rws = []
for i in range(1):
    rws.append(RandomWalk())

for i, rw in enumerate(rws):
    #  plt.figure(i)
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9))
    point_numbers = range(rw.max_steps)
    ax.scatter(rw.x_vals, rw.y_vals, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_vals[-1], rw.y_vals[-1], c='red', edgecolors='none', s=100)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
