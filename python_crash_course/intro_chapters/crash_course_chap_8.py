# Examples and Notes from Python Crash Course
# Chapters 8
# Created 2020-04-09
# Last modified 2020-04-13

from tony_functions import *
#from printing_models import *  # used before functions were in a seperate file
#import printing_models # problem 18-16a
#from printing_models import make_car # problem 18-16b
#from printing_models import make_car as mc # problem 18-16c
#import printing_models as pm # problem 18-16d
from printing_models import * # problem 18-16e


def prob_8_7():
	describe_pet1('cat', 'momma cat')
	describe_pet1(pet_name='battle cat', animal_type='tiger')
	describe_pet2('bebe')
	describe_pet2('bebe', 'rat terrier')

	make_shirt('large', 'honk if you are horny')
	make_shirt(text="I have no idea whats going on", size='extra small')
	make_shirt()
	make_shirt('medium')
	make_shirt('extra large', 'i beat anorexia')

	describe_city('toranto', 'canada')
	describe_city('sacramento')
	describe_city(country='japan', city='tokyo')

	city_country('hard_to_spell', 'iceland')


	print(make_album('prince', 'purple rain'))
	print(make_album('talking heads', 'remain in light', 8))


def prob_8_9():
	messages = ['i', 'think', 'her', 'name', 'was', 'brabra']
	print_messages(messages)

def prob_8_10():
	messages = ['john', 'paul', 'geroge', 'ringo']
	print(f'preparing to send message list:\n{messages}')
	sent = send_messages1(messages)
	print(f'original message list:\n{messages}')
	print(f'sent message list:\n{sent}')

def prob_8_11():
	messages = ['john', 'paul', 'geroge', 'ringo']
	print(f'preparing to send message list:\n{messages}')
	sent = send_messages2(messages)
	print(f'original message list:\n{messages}')
	print(f'sent message list:\n{sent}')

def page_143():
	make_pizza(12, 'mushrooms')
	make_pizza(14, 'mushrooms', 'pinnaple', 'olives')
	topping_list = ['cheese', 'anchovies', 'peppers']
	make_pizza(16, *topping_list[:])
	make_pizza(20)

def prob_8_12():
	samich('bread', 'lettuce', 'tomatoe')
	samich('cheese')
	samich()

def prob_8_13():
	aeh1 = {"height": "6'4\"", 'weight': '205'}
	#aeh2 = user_profile('tony', 'held', **aeh1)
	aeh2 = user_profile('tony', 'held', height='6\'4"', weight='205')
	print(f'aeh1: {aeh1}')
	print(f'aeh2: {aeh2}')

def prob_8_14():
	car = make_car('subaru', 'outback', color='blue', tow_package=True)
	print(car)

def prob_8_16a():
	car = printing_models.make_car('subaru', 'outback', color='blue', tow_package=True)
	print(car)

def prob_8_16b():
	car = make_car('subaru', 'outback', color='blue', tow_package=True)
	print(car)

def prob_8_16c():
	car = mc('subaru', 'outback', color='blue', tow_package=True)
	print(car)

def prob_8_16d():
	car = pm.make_car('subaru', 'outback', color='blue', tow_package=True)
	print(car)

def prob_8_16e():
	car = make_car('subaru', 'outback', color='blue', tow_package=True)
	print(car)

print_header("Chapter 8 - Functions")
#prob_8_7()
print_header("Betsy is Super Mega Great", 'w')

#prob_8_9()
#prob_8_10()
#prob_8_11()
#page_143()
#prob_8_12()
#prob_8_13()
#prob_8_14()
#prob_8_16a()
#prob_8_16b()
#prob_8_16c()
#prob_8_16d()
prob_8_16e()