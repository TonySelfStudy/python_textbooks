# Examples and Notes from Python Crash Course
# Chapters 10
# Created 2020-04-15
# Last modified 2020-04-14

def page_184():

	with open('pi_digits.txt') as file_object:
		contents = file_object.read()
	print(contents.rstrip())

	filename = 'pi_digits.txt'

	with open(filename) as file_object:
		for line in file_object:
			print(line.strip())

	with open(filename) as file_object:
		lines = file_object.readlines()

	str_pi = ''

	for line in lines:
		str_pi+=line.strip()

	print(f'{str_pi}')
	print(f'{len(str_pi)}')

def page_190():

	filename = 'pi_million_digits.txt'
	pi_str=''

	with open(filename) as file_object:
		for line in file_object:
			pi_str += line.strip()

	print(f'{pi_str[:52]} ...\n')

	birthday='040581'
	#birthday='071172'

	b_index = pi_str.find(birthday)
	#print(f'index= {b_index}')

	for i in range(b_index, b_index+6):
		print(f'{i}: {pi_str[i]}')

	if birthday in pi_str:
		print('\nIt is in there!\n')
	else:
		print('\nIt is NOT in there!\n')

def prob_10_1():
	filename = 'learning_python.txt'

	print(f'Reading file into a single string')
	with open(filename) as file_object:
		str1=file_object.read()
	print(f'{str1}')

	print(f'Reading file line by line')
	with open(filename) as file_object:
		for line in file_object:
			print(line.rstrip())
	print(f'')

	print(f'Reading file into list')
	with open(filename) as file_object:
		lines= file_object.readlines()

	for line in lines:
		print(f'{line.rstrip()}')
	print(f'')


	for line in lines:
		str1 = line.replace('Python', 'Java').rstrip()
		print(f'{str1}')

def page_191():
	filename='pyton_output.txt'
	with open(filename, 'w') as file_object:
		file_object.write('Line 1.\n')
		file_object.write('Line 2.\n')
		file_object.write('Line 3.\n')

	with open(filename, 'a') as file_object:
		file_object.write('Line 4.\n')
		file_object.write('Line 5.\n')
		file_object.write('Line 6.\n')

def prob_10_1():
	pass

def page_194():
	try:
		print(5/2)
		print(f'{missing_variable}')
		print(5/0)
		print(5/3)

	except FileNotFoundError:
		print("FileNotFoundError!")
	except ZeroDivisionError:
		print("ZeroDivisionError!")
	except:
		print("General Error!")
	else:
		print("You made it past the error handler!")

def prob_10_6():

	try:
		str0='cat'
		str1='1'
		str2='2'
		str3= str1 + str2
		print(f'adding strings result: {str3}')
		int1= int(str1)
		int2= int(str2)
		int3= int1+int2
		print(f'adding strings result: {int3}')
		int0= int(str0)
	except ValueError:
		print(f"ValueError.  Can't convert '{str0}'' to an integer")
	
def prob_10_8():
	filenames=['cats.txt', 'dogs1.txt']

	for filename in filenames:
		print(f'Attempting to open file: {filename}')

		try:
			with open(filename) as f:
				str1=f.read()
				print(f'File contents are:')
				print(f'{str1}\n')
		except FileNotFoundError as e:
			print(f'File not found: {filename}')
			print(f'{e}')

def prob_10_10():
	filename='treasure_island.txt'
	try:
		with open(filename, encoding='utf8') as f:
			str1=f.read()
	except FileNotFoundError as e:
		print(f'FileNotFoundError trying to open {filename}')
		return

	count=str1.lower().count('the')
	print(f"The word 'the' appears approximately {count} times in {filename}")

	count=str1.lower().count('cat')
	print(f"The word 'cat' appears approximately {count} times in {filename}")

	count=str1.lower().count('pig')
	print(f"The word 'pig' appears approximately {count} times in {filename}")

def page_202():
	pass

#page_184()
page_190()
#prob_10_1()
#page_191()
#prob_10_1()
#page_194()
#prob_10_6()
#prob_10_8()
# prob_10_10()
#page_202()
