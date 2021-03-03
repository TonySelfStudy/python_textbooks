# Examples and Notes from Python Crash Course
# Chapters 5
# Created 2020-04-08
# Last modified 2020-04-08

from tony_functions import *

print_header("Chapter 5 - Working with IF Statements")

# cars = ['audi', 'bmw', 'subaru', 'toyota']

# for car in cars:
# 	if car=='bmw':
# 		print(car.upper())
# 	else:
# 		print(car.title())

# car_choice = 'ford'

# if car_choice in cars:
# 	print(f"{car_choice} is in the list cars")
# else:
# 	print(f"{car_choice} is not in the list cars")

# car_choice = 'ford'

# if car_choice not in cars:
# 	print(f"{car_choice} would be a new addition to the list cars")
# else:
# 	print(f"{car_choice} is already in the list cars")

# if False:
# 	print("I'm a little teacup")
# else:
# 	print("I guess I'm not a little teacup")

# ages = list(range(1,101,10))

# for age in ages:
# 	if age<4:
# 		print(f"Your age is {age} which is less than 4, so it is free admission")
# 	elif age<=18:
# 		print(f"Your age is {age} which is between 4 and 18 , so your admission is $25")
# 	elif age>18:
# 		print(f"Your age is {age} is 18 or older, so your admission is $40")

# alien_colors=['green', 'yellow', 'red', 'blue']

# for alien_color in alien_colors:
# 	if alien_color=='green':
# 		points=5
# 	elif alien_color=='yellow':
# 		points=10
# 	elif alien_color=='red':
# 		points=15
# 	else:
# 		points = 0
# 	print(f"You shot down a {alien_color} worth {points} points")

user_names1=['Bashful', 'Doc', 'Grumpy', 'Happy', 'Sneezy', 'Sleepy', 'Dopey', 'admin']
user_names2=[]
user_names3=['thundar', 'ariel', 'ookla']
user_names4=user_names1[:3] + user_names3
all_user_names = [user_names1, user_names2, user_names3]

for sublist in all_user_names:
	if sublist:
		for user_name in sublist:
			if user_name=="admin":
				print(f'Welcome {user_name}, would you like to see a status report?')
			else:
				print(f'Hello {user_name}, thanks for logging in!')
	else:
		print('\n*** Sublist is empty ***\n')

current_users = user_names1
new_users = user_names4

print(f'current users: {current_users}')
print(f'new users: {new_users}')
print('processing new users ...')

if len(current_users)>0 and len(new_users)>0:
	for new_user in new_users:
		print(f'processing potential user name: {new_user}')
		if new_user in current_users:
			print('f(user name:{new_user} is already taken, pick another')
		else:
			print('f(user name:{new_user} is available and added to current users list')
			current_users.append(new_user)
		
print('new users added to current users list')
print(f'the new current users: {current_users}')


print('Printing ordinals')
ordinals = list(range(1,10))

for ordinal in ordinals:
	if ordinal==1:
		print(f'{ordinal}st', end =" ")	
	elif ordinal==2:
		print(f'{ordinal}nd', end =" ")
	elif ordinal==3:
		print(f'{ordinal}rd', end =" ")
	else:
		print(f'{ordinal}th', end =" ")
print('\nOrdinals complete')
