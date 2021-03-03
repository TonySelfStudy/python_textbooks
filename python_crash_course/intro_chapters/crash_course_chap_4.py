# Examples and Notes from Python Crash Course
# Chapters 4
# Created 2020-04-08
# Last modified 2020-04-09

print("Chapter 4 Working with Lists")
print("****************************")


print("\nExercise 4-1")
print("************")

# magicians = [ 'alice', 'david', 'carolina']
# print(f'Original magicians: {magicians}')
# for magician in magicians:
# 	print(f"{magician.title()} is going to do a trick")
# print(f'Thanks for the tricks, that was a great show\n')

# pizzas = ['cheese', 'mushroom', 'veggie']

# for pizza in pizzas:
# 	print(f"I like {pizza} pizzas!")
# print("I guess it turns out I like pizza a lot")

# print("\nWorking with Range Functions")
# print("************")

# for value in range(5):
# 	print(value)

# numbers = list(range(1,6))
# print(numbers)

# for n in numbers:
# 	print(n)

# squares=[]
# num_squares=15
# for i in range(1,num_squares+1):
# 	squares.append(i*i)
# print(f"the first {len(squares)} squares are \n {squares}")
# print(f"their min is: {min(squares)}")
# print(f"their max is: {max(squares)}")
# print(f"their sum is: {sum(squares)}")
# print(f"their average is: {sum(squares)/len(squares)}")

print("\nExercise 4-3")
print("************")

# for i in range(1,21):
# 	print(i)

# first_million=list(range(1,1_000_001))
# print(f"the list first_million has a length of: {len(first_million)}")
# print(f"its min is {min(first_million)} and its max is {max(first_million)}")
# print(f"its sum is {sum(first_million)} ")

# odds=list(range(1,20,2))
# for i in odds:
# 	print(i)

# print(f"shooting for 3s")
# threes=list(range(3,31,3))
# for i in threes:
# 	print(i)

# print(f"cubing")
# myrange=range(1,11)
# print(f"myrange:{myrange}")
# cubes=[]
# cubes_bases=list(myrange)
# for i in cubes_bases:
# 	cubes.append(i**3)
# for i in myrange:
# 	print(f"{cubes_bases[i-1]}s cube is {cubes[i-1]}")

# cube2 = [i**3 for i in range(1,11)]
# print(f"cube2 is:{cube2}")

# # for i in first_million:
# # 	print(i)

print("\nExercise Slices")
print("*****************")


# players=['charles','martina','michael','florence','eli']
# print(players)
# print(players[0:3])

# for player in players[-3:]:
# 	print(player)

cube2 = [i**3 for i in range(1,11)]
print(f"cube2 is:{cube2}")

print(f"the first 3 cubes are {cube2[:3]}")
print(f"3 mid cubes are {cube2[3:6]}")
print(f"The last 3 cubes are {cube2[-3:]}")


pizzas = ['cheese', 'mushroom', 'veggie']
friend_pizzas = pizzas[:]
pizzas.append('pinapple')
friend_pizzas.append('fake sausage')
for i in range(len(pizzas)):
	print(f"i={i} pizzas[{i}]={pizzas[i]} \tfriend_pizzas[{i}]={friend_pizzas[i]}")

dimentions = (200, 50)
print(f"dimentions={dimentions}")

touple1=3,
print(f"len of touple1={len(touple1)}")
print(f"touple1={touple1}")
touple1=[4]
print(f"len of touple1={len(touple1)}")
print(f"touple1={touple1}")

five_foods=('salad', 'eggs', 'cheese', 'salsa', 'chips') #touple

header='\nOriginal Menu'
print(f"{header}\n{'-'*len(header)}")  #Turn this into a function sometime

i=0
for food in five_foods:
	print(f"food[{i}]={food}")
	i=i+1

five_foods=('salad', 'carrots', 'vegan cheese', 'salsa', 'chips') #touple

header='\nRevised Menu'
print(f"{header}\n{'-'*len(header)}")  #Turn this into a function sometime

i=0
for food in five_foods:
	print(f"food[{i}]={food}")
	i=i+1