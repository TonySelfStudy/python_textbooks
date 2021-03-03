class User:
	"""Class for solving problem 9-3"""
	def __init__(
		self, first_name, last_name, 
		city='sacramento', state='ca', joined='2020'):

		self.first_name = first_name
		self.last_name = last_name
		self.city =  city
		self.state =  state
		self.joined =  joined
		self.login_attempts = 0

	def describe_user(self):
		print(f'**Describing user from User**')
		for key, value in vars(self).items():
			print(f'{key}\t = {value}')

	def greet_user(self):
		print(f'Greetings {self.first_name}, {self.last_name}!  '
			f'Thank you for being a user since {self.joined}.')

	def login(self):
		self.login_attempts +=1
		print(f'This is your {self.login_attempts} login attempt')
		self.greet_user()


