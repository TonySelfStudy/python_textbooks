# Examples and Notes from Python Crash Course
# Chapters 7
# Created 2020-04-09
# Last modified 2020-04-09

from tony_functions import *

print_header("Chapter 7 - User input and while loops")

# message = input("How many in your party: ")
# guests= int(message)
# if guests >= 8:
# 	print(f"For a party of {guests} you will have to wait for a table")
# else:
# 	print(f"Your table for {guests} people is ready now")

# prompt = "Lets see if a given number is a multiple of 10"
# prompt += "\nWhat number would you like to try? "

# message = input(prompt)
# val=int(message)
# remainder = val % 10

# if remainder == 0:
# 	print(f'{val} is a multiple of 10')
# else:
# 	print(f'{val} is not a multiple of 10')
# 	print(f'it has a remainder of {remainder}.')

# i =0
# while i<=5:
# 	print(f'i={i}')
# 	i+=1

# print("please enter your favorite pizza toppings")
# print("enter quit to end your submission")

# toppings = []
# active=True
# while active:
# 	topping = input('Topping: ')
# 	if topping=='quit':
# 		break
# 	toppings.append(topping)
# if len(toppings)==0:
# 	print("whats the matter with you, add some pizza toppings next time!")
# else:
# 	print(f"You selected these toppings: \n {toppings}")

# print('We are out of pastrami!\n')
# sandwich_orders = ['pastrami', 'grilled cheese', 'pastrami', 'veggie', 'avocado', 'MLT', 'pastrami']
# finished_sandwiches = []
# pastrami_count =0

# while len(sandwich_orders)>0:
# 	current_sandwich = sandwich_orders.pop(0)
# 	if current_sandwich == 'pastrami':
# 		print("wassamatta you, i said we aint go no pastrami!")
# 		pastrami_count +=1
# 	else:
# 		print(f"i'm now making a {current_sandwich} sandwich.")
# 		finished_sandwiches.append(current_sandwich)

# print('Sandwich making complete, I made the following sandwiches')
# for sandwich in finished_sandwiches:
# 	print(f'{sandwich}')
# print(f'{pastrami_count} bozos asked for pastrami even though we are out!')


