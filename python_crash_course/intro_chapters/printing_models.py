# Examples and Notes from Python Crash Course
# Chapters 8 Functions

def describe_pet1(animal_type, pet_name):
	"""example from page 132"""
	print(f"I have an {animal_type} named {pet_name}")

def describe_pet2(pet_name, animal_type='dog'):
	"""example from page 132"""
	print(f"I have an {animal_type} named {pet_name}")

def make_shirt(size='large', text='i love python'):
	print(f"A {size} size shirt has been ordered with the caption:\n'{text}'")

def describe_city(city, country='USA'):
	print(f'{city} is in {country}')

def city_country(city, country):
	print(f'{city.title()}, {country.title()}')

def make_album(artist, album, number_songs=None):
	temp = {'artist': artist, 'album': album}
	if number_songs:
		temp['number_songs']=number_songs
	return temp


def print_messages(messages):
	for message in messages:
		print(f'{message}')

def send_messages1(messages):   #remove original messages
	sent=[]
	while messages:
		curent_message = messages.pop()
		print(f'Sending message: {curent_message}')
		sent.append(curent_message)
	return sent

def send_messages2(messages):   #keep original messages
	sent=[]
	for message in messages:
		print(f'Sending message: {message}')
		sent.append(message)
	return sent


def make_pizza(size, *toppings):
	print(f"making a {size} inch pizza")
	if toppings:
		print('with toppings')
		for topping in toppings:
			print(f" -{topping}")

def samich(*ingredients):
	print(f'You ordered a sandwich with {len(ingredients)} ingredients')
	for ingredient in ingredients:
		print(f' -{ingredient}')

def user_profile(first, last, **user_info):
	user_info['first name']= first
	user_info['last name']= last
	return user_info

def make_car(
			manufacturer, 
			model, 
			**car_info):
	car_info['manufacturer']= manufacturer
	car_info['model']= model
	return car_info
