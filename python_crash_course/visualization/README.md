Data Visualization Practice

Based on learning exercise from 'Python Crash Course Version 2'

Make sure you install the ** package first with the command:

python -m pip install --user matplotlib

To run game, execute the following from a command line in the project directory:

**

Created by: Tony Held, tony.held@gmail.com

Note: Interactive mode determines how a plot is updated.
its value may be queried via matplotlib.is_interactive(). 
It may also be set via matplotlib.interactive(),
Interactive mode may also be turned on via matplotlib.pyplot.ion(), 
and turned off via matplotlib.pyplot.ioff().

From: https://medium.com/@1522933668924/using-matplotlib-in-jupyter-notebooks-comparing-methods-and-some-tips-python-c38e85b40ba1

Option 1: Use %matplotlib notebook to get zoom-able & resize-able notebook. This is the best for quick tests where you need to work interactively.

Option 3: Use %matplotlibe inline - this only draws the images, not interactive / zoom-able but it works well. I recommend to change figure size to be bigger than the default in most cases (see notes below on how).


read about numpy
https://numpy.org/doc/stable/

read about matplotlib
https://matplotlib.org/3.2.1/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py

read about plotly
https://plotly.com/python/
