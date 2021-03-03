# Examples and Notes from Python Crash Course
# Chapters 3
# Created 2020-04-08
# Last modified 2020-04-08

print("Chapter 3 Introducing Lists")
print("***************************")


# Examples on Page 36
print("\nExercise 3-1")
print("************")

# bikes = ['trek', 'connondale', 'redline', 'specialized']
# print(bikes)
# print("bike 1 is: " + bikes[0].title())
# print("bike 2 is: " + bikes[1].title())
# print("bike 3 is: " + bikes[2].title())
# print("the last bike is: " + bikes[-1].title())
# print(f"My first bike was a {bikes[0].upper()}\n")

# motorcycles =  ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# motorcycles.append('ducati')
# print(motorcycles)

# motorcycles.insert(0,'ducati')
# print(motorcycles)

# del motorcycles[1]
# print(motorcycles)

# pop_cycle = motorcycles.pop()
# print('the popped cycle is: ' + pop_cycle)
# print(f'the motocycle array is now: {motorcycles}')

# too_expensive='ducati'
# motorcycles.remove(too_expensive)
# print(f'I have removed the {too_expensive} because it was too expensive')
# print(f'My bike collection is now {motorcycles}')


print("\nExercise 3-4")
print("************")

# invites=['prince', '7 of 9', 'lincoln' ]
# print(f"The original guest list is: {invites} ")
# print(f'Hiya {invites[0].title()}, would you like to come over for dinner?')
# print(f'Hiya {invites[1].title()}, would you like to come over for dinner?')
# print(f'Hiya {invites[2].title()}, would you like to come over for dinner?')

# cant_attend=invites.pop(0)
# can_attend='weird al'
# invites.append(can_attend)

# print(f"\nUnfortunately {cant_attend.title()} can't make it")
# print(f"So he will be replaced with {can_attend.title()}")
# print(f"The new guest list is: {invites} ")

# cant_attend='7 of 9'
# can_attend='wilma dearing'
# invites.remove(cant_attend)
# invites.append(can_attend)

# print(f"\nUnfortunately {cant_attend.title()} can't make it")
# print(f"So she will be replaced with {can_attend.title()}")
# print(f"The new guest list is: {invites} ")

print("\nExercise 3-8")
print("************")

# cars=['bmw', 'audi', 'toyota', 'subaru']
# print(f'The list cars is: {cars}')

# print('sorting the cars now ...')
# cars.sort()
# print(f'The list cars is: {cars}')

# print('reverse sorting the cars now ...')
# cars.sort(reverse=True)
# print(f'The list cars is: {cars}')

# cars=['bmw', 'audi', 'toyota', 'subaru']
# print(f'\nThe list cars is again: {cars}')

# print('reverse ordering the cars now ...')
# cars.reverse()
# print(f'The list cars is: {cars}')

# len_cars = len(cars)
# print(f'The length of the list cars is: {len_cars}')


locations =['crater lake', 'banff', 'hawaii', 'samoa', 'new orleans']
len_locations = len(locations)
print(f'The list of travel locations is: {locations}')
print(f'The # of locations in the list is: {len_locations}')
print(f'The sorted list is: {sorted(locations)}')
print(f'The original is still: {locations}')
print(f'The reverse sorted list is: {sorted(locations, reverse=True)}')
print(f'The original is still: {locations}')
print(f'reversing the order of the list')
locations.reverse()
print(f'The reverse order list is: {locations}')
print(f'reversing the order of the list again')
locations.reverse()
print(f'The double reverse order list is: {locations}')
print(f'\npermanantly sorting the order of the list')
locations.sort()
print(f'The sorted list is: {locations}')
print(f'permanantly reverse sorting the order of the list')
locations.sort(reverse=True)
print(f'The sorted list is: {locations}')



