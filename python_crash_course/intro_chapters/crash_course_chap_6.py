# Examples and Notes from Python Crash Course
# Chapters 6
# Created 2020-04-09
# Last modified 2020-04-09

from tony_functions import *

print_header("Chapter 6 - Working with Dictionaries")

# alien_0 = {'color': 'green', 'points': 5}
# alien_0['x_pos'] = 0
# alien_0['y_pos'] = 25
# print(alien_0)

# alien_0['color']='yellow'
# print(alien_0)

# alien_1 = {'x_pos': 0, 'y_pos': 0, 'speed': 'fast'}
# print(alien_1)

# # move the alien
# alien_speed=alien_1['speed']

# if alien_speed == "slow":
# 	alien_1['x_pos'] +=1
# elif alien_speed == "medium":
# 	alien_1['x_pos'] +=2
# elif alien_speed == "fast":
# 	alien_1['x_pos'] +=3

# print(alien_1)

# del alien_1['speed']
# print(alien_1)

# fav_languages = {
# 	'jen': 'python',
# 	'sarah': 'c',
# 	'edward': 'ruby',
# 	'phil': 'python',
# }

# person1={
# 	'first_name': 'dave',
# 	'last_name': 'held',
# 	'age': 76,
# 	'city': 'san antonio'
# }
# print(person1)

# for k,v in fav_languages.items():
# 	print(f"{k.title()}'s favorite language is {v.upper()} ")

# i=0
# for v in fav_languages.values():
# 	i+=1
# 	print(f"value {i} is {v.upper()} ")

# friends = ['phil', 'sarah', 'edward', 'tony', 'bebe']

# for friend in friends:
# 	friend_lang =fav_languages.get(friend)
# 	if friend_lang==None:
# 		print(f"The favorite language of {friend} is unknown")
# 	else:
# 		print(f"The favorite language of {friend} is {friend_lang}")

# for person in sorted(fav_languages.keys()):
# 	print(f"Hi {person}!")

# for language in set(fav_languages.values()):
# 	print(f"{language.upper()}")

# print_header("Problem 6.4")

# glossary = {
# 	'pop': 'pull the last off the stack',
# 	'elif': 'stranger things character',
# 	'hash': 'what i had for breakfast',
# 	'list': 'the think a kiss is on',
# 	'ruby': 'dark shining jewell'
# }

# glossary[0]='not the same as none'
# glossary['multi']= ['a', 'list', 'can', 'be', 'a', 'value']

# for k,v in glossary.items():
# 	print(f"{k}: {v}")

# print_header("\nProblem 6.5")

# rivers={'nile': 'egypt', 'sacramento': 'USA', 'amazon': ['brazil', 'equador', 'colombia', 'colombia']}
# #rivers['amazon']='brazil'

# for river, country in rivers.items():
# 	if type(country) is list:
# 		pcountry = set([x.title() for x in country])  #capitalize list
# 		pcountry = ', '.join(pcountry)  # join with commas
# 	else:
# 		pcountry = country.title()
# 	print(f"The river {river.upper()} runs through {pcountry}.")

# print(f"\nThe rivers considered are:")
# for k in rivers:
# 	print(f"{k.title()}")

# print(f"\nThe countries considered are:")
# countries=[]
# for c in rivers.values():
# 	if type(c) is list:
# 		countries.extend(c)
# 	else:
# 		countries.append(c)
# fcountries = [x.title() for x in countries]
# fcountries.sort()

# for c in set(sorted(fcountries)):
# 	print(f"{c}")

# print_header("\nProblem 6.6")

# fav_languages = {
# 	'jen': 'python',
# 	'sarah': 'c',
# 	'edward': 'ruby',
# 	'phil': 'python',
# }

# friends = ['phil', 'sarah', 'edward', 'tony', 'bebe']

# fav_people = list(fav_languages.keys())
# print(f'fav people {fav_people}')
# all_people = fav_people[:]
# all_people.extend(friends) 
# print(f'all people {all_people}')
# all_people = set(all_people) 
# print(f'all people - no duplicates {all_people}')

# for person in all_people:
# 	fav_lang = fav_languages.get(person)
# 	if fav_lang==None:
# 		print(f"{person}, please consider participating in a language poll")
# 	else:
# 		print(f"{person}, your favorite language is {fav_lang}, thanks for responding to the poll")

print_header("Fun with nesting")

# alien_0={'color':'green', 'points': 5}
# alien_1={'color':'yellow', 'points': 10}
# alien_2={'color':'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
# 		print(alien)


# person0={
# 	'first_name': 'dave',
# 	'last_name': 'held',
# 	'age': 76,
# 	'city': 'san antonio'
# }

# person1={
# 	'first_name': 'bob',
# 	'last_name': 'smith',
# 	'age': 25,
# 	'city': 'san diego'
# }

# person2={
# 	'first_name': 'jane',
# 	'last_name': 'austin',
# 	'age': 125,
# 	'city': 'london'
# }

# people=[person0, person1, person1]
# i=0
# for person in people:
# 	print(f'Person {i}s information')
# 	i+=1
# 	for k, v in person.items():
# 		print(f'{k}={v}')

# print('\nFun with pets\n')
# pet0 = {'breed': 'terrier', 'age': 16, 'owner': 'tony'}
# pet1 = {'breed': 'dachshund', 'age': 5, 'owner': 'britany'}
# pet2 = {'breed': 'mut', 'age': 1, 'owner': 'buzz'}

# pets = [pet0, pet1, pet2]

# for pet in pets:
# 	for k, v in pet.items():
# 		print(f'{k}={v}')
# 	print()

# favorite_places={
# 	'peep1': 'place1',
# 	'peep2': ['place2', 'place3'],
# 	'peep3': ['place4', 'place5', 'place6']
# }

# for name, places in favorite_places.items():
# 	print(f"{name}'s favorite place(s) is/are {places}")
# 	print(f'length of places is {len(places)}')


cities = {
	'sacramento': 	{'county': 'sacto',
					 'population': 4000000,
					 'fact': 'i live here'},
	'san diego': 	{'county': 'sandag',
					 'population': 6000000,
					 'fact': 'matt lives there'},
	'plymouth': 	{'county': 'placer',
					 'population': 4000,
					 'fact': 's&d live there'}
}

for city, info in cities.items():
	print(f'City name = {city}')
	for k,v in info.items():
		print(f'{k}={v}')
	print()

