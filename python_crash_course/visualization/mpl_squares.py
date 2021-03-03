import matplotlib.pyplot as plt
from tony_functions import *

print_header('Chapter 15, Starting Page = 306')
print(f'interactive mode is: {plt.isinteractive()}')
plt.ioff()
print(f'interactive mode is: {plt.isinteractive()}')

input_values = range(1,1001)
squares = [i**2 for i in input_values]
cubes = [i**3 for i in input_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

# ax.scatter(2, 4, s=200)
# ax.plot(input_values, squares, linewidth=3)
ax.scatter(input_values, cubes, c=cubes, cmap=plt.cm.flag,   s=10)

ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
# ax.axis([0, 1100, 0, 1100000])

plt.show()
ax.set_title("Cube Numbers Revised", fontsize=24)
plt.show()

# plt.savefig('squares_plot.png', bbox_inches='tight')

print('after the show')



