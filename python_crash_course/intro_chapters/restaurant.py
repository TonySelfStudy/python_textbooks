class Restaurant:
	"""class for problem 9-1"""
	def __init__(self, restaurant_name, cuisine_type):
		print(f'Creating a restaurant named {restaurant_name} '
			f'which makes {cuisine_type} food')
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served=0

	def serve_customers(self, new_customers):
		self.number_served += new_customers
		print(f'Now serving {new_customers} new customers. '
			f'Total customers served= {self.number_served}')
		

	def describe_restaurant(self):
		print(f'Restaurant name: {self.restaurant_name}\n'
			f'Cuisine type: {self.cuisine_type}')

	def open_restaurant(self):
		print(f'{self.restaurant_name} is now open!')

class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name):
		super().__init__(restaurant_name, 'Ice Cream Stand')
		self.flavors=[] # blank list of flavors

	def add_flavors(self, *flavors):
		for flavor in flavors:
			self.flavors.append(flavor)
			print(f'flavor: {flavor} has been added')


	def show_flavors(self):
		print(f'The current flavors are: {self.flavors}')


