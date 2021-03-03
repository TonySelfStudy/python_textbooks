class Car:

	def __init__(self, make, model, year):
		self.make=make
		self.model=model
		self.year=year
		self.odometer=0

	def longname(self):
		rname=f'{self.make}, {self.model}, {self.year}'
		return rname

	def update_odometer(self, milage):
		if milage<self.odometer:
			print(f"You can't rollback the odometer from {self.odometer} to {milage}")
		else:
			self.odometer = milage

	def print_odometer(self):
		print(f'The car has {self.odometer} miles.')

class Battery():
	MILES_PER_WATT = 50

	def __init__(self, b_size=75):
		self.b_size=b_size
		self.b_range=b_size*Battery.MILES_PER_WATT

	def upgrade_battery(self):
		min_watts = 100
		if self.b_size<min_watts:
			print(f'battery of size {self.b_size} upgraded to {min_watts} minimum watts')
			self.b_size=min_watts
			self.b_range=self.b_size*Battery.MILES_PER_WATT

	def describe_battery(self):
		return f'Battery size = {self.b_size} watts, battery range={self.b_range} miles'

class ElectricCar(Car):
	def __init__(self, make, model, year, battery_size):
		super().__init__(make, model, year)
		self.battery= Battery(battery_size) #in watts

	def longname(self):
		rname=f'{self.make}, {self.model}, {self.year}, {self.battery.describe_battery()}'
		return rname

