# Examples and Notes from Python Crash Course
# Chapters 9
# Created 2020-04-13
# Last modified 2020-04-13

from tony_functions import *
from dog import Dog
from restaurant import Restaurant
from restaurant import IceCreamStand
from user import User
from privileges_and_admin import Admin
from car import Car
from car import ElectricCar


def prob_page158():
	my_dog = Dog('Willie', 8)
	print(f"Hi doggie named: {my_dog.name}")
	my_dog.sit()
	my_dog.sit()
	my_dog.roll_over()
	my_dog.diagnostic()

def prob_9_1():
	my_restaurant1 = Restaurant("Luigi's", "Italian")
	my_restaurant1.describe_restaurant()
	my_restaurant1.open_restaurant()

def prob_9_3():
	user1=User('tony', 'held')
	user1=User('ryan', 'meek', 'austin', joined=2021)
	user1.describe_user()
	user1.greet_user()

def page_162():
	my_car = Car('audi', 'a4', 2019)
	print(f"|{my_car.longname()}|")
	my_car.update_odometer(123)
	my_car.print_odometer()
	my_car.update_odometer(111)
	my_car.print_odometer()
	my_car.odometer=99 # can directly access odometer and break encapsulation
	my_car.print_odometer()
	my_car.odometer+=99
	my_car.print_odometer()

def prob_9_4():
	my_restaurant1 = Restaurant("Luigi's", "Italian")
	my_restaurant1.serve_customers(5)
	my_restaurant1.serve_customers(7)

def prob_9_5():
	user1=User('ryan', 'meek', 'austin', joined=2021)
	user1.login()
	user1.login()
	user1.login()

def prob_9_6():
	ice1 = IceCreamStand('Pops')
	ice1.describe_restaurant()
	ice1.add_flavors('vanilla')
	ice1.show_flavors()
	ice1.add_flavors('chocolate', 'strawberry', 'peanut butter')
	ice1.show_flavors()

def prob_9_7():
	admin1=Admin('ryan', 'meek', 'austin', 'texas', joined=2021)
	admin1.describe_user()
	admin1.show_privileges()

def prob_9_9():
	my_ecar = ElectricCar('tesla', 'model s', 2019, 75)
	print(f"|{my_ecar.longname()}|")
	my_ecar.update_odometer(123)
	my_ecar.print_odometer()
	my_ecar.battery.upgrade_battery()
	print(f"|{my_ecar.longname()}|")
	
def page_180():
	pass


print_header("Fun with Classes","*")

#prob_page158()
#prob_9_1()
#prob_9_3()
#page_162()
#prob_9_4()
#prob_9_5()
#prob_9_6()
#prob_9_7()
#prob_9_9()
page_180()
