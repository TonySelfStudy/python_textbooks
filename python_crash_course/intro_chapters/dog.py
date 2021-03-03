class Dog:
	"""A simple attempt to model a dog"""
	def __init__(self, name, age):
		print(f'Creating a dog with name: {name} of age {age}')
		self.name = name
		self.age = age
		self.sit_count = 0
		self.roll_count = 0

	def sit(self):
		print(f'{self.name} is now sitting')
		self.sit_count +=1

	def roll_over(self):
		print(f'{self.name} is now rolling over')
		self.roll_count +=1

	def diagnostic(self):
		print(f"The dog '{self.name}' age {self.age} "
			f"has sat {self.sit_count} times and "
			f"rolled over {self.roll_count} times.")