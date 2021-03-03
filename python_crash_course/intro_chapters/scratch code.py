			attempts += 1
			for i in range(0,DChar.NUM_QUALITIES):
				temp_roll[i]= 3
			min_roll = min(temp_roll) 
			if attempts == 100000:
				print(f'could not find a good roll in 100000 attempts')
				min_roll=18

				
		# but randint is very slow in python, and it is better to 
		# call the underlying c routine with less overhead as show below
		# floor(n*random()) to compute an integer in [0, n)
		# add 3 since you want each roll to be 1 to 6 not 0 to 5


		return floor(5*random()) + floor(5*random()) + floor(5*random()) + 3
		from math import floor
		from random import random


		# I would like to implement the code with the following line,