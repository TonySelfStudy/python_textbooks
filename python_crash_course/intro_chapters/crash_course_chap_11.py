# Examples and Notes from Python Crash Course
# Chapters 11
# Created 2020-04-16
# Last modified 2020-04-16

from tony_functions import *
import unittest

print_header("Chapter 11 Testing Code")

def get_formatted_name(first, last, middle=''):
	"""Generate a neatly formatted full name"""
	if middle:
		full_name=f'{first} {middle} {last}'
	else:
		full_name=f'{first} {last}'
	return full_name.title()

def page_210():
	names = [['jimi', 'henrix', 'maddog' ], 
			['janis', 'joplin'],
			['bob', 'dylan', 'acoustic']]
	for name in names:
		str1=get_formatted_name(*name)
		print(f'{str1}')

class TestFormatFunction(unittest.TestCase):
	"""class to test get_formatted_name function"""
	def test_first_last_name(self):
		formatted_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')

	def test_first_last_middle_name(self):
		formatted_name = get_formatted_name('john', 'hooker', 'lee')
		self.assertEqual(formatted_name, 'John Lee Hooker')

def format_city(city, country, population=-1):
	if population==-1:
		formatted_name=f'{city.title()}, {country.title()}'
	else:
		formatted_name=f'{city.title()}, {country.title()} with a population of {population}'
	return formatted_name

class TestCities(unittest.TestCase):
	def test_city_country(self):
		formatted_name = format_city('santiago', 'chile')
		self.assertEqual(formatted_name, 'Santiago, Chile')
	def test_city_country_population(self):
		formatted_name = format_city('santiago', 'chile', 400000)
		self.assertEqual(formatted_name, 'Santiago, Chile with a population of 400000')


class Employee():
	def __init__(self, first_name, last_name, salary):
		self.first_name = first_name
		self.last_name = last_name
		self.salary = salary
	def print_employee(self):
		print(f'{self.first_name} {self.first_name} makes {self.salary} per year.')
	def give_raise(self, raise1=5000):
		self.salary += raise1

class TestEmployee(unittest.TestCase):
	def setUp(self):
		self.emp1= Employee('john', 'doe', 30000)
		self.emp1.print_employee()

	def test_raise_default(self):
		self.emp1.give_raise()
		self.assertEqual(self.emp1.salary, 35000)
	def test_raise(self):
		self.emp1.give_raise(10000)
		self.assertEqual(self.emp1.salary, 40000)


#page_210()

	emp1= Employee('john', 'doe', 30000)
	emp1.print_employee()

if __name__ == '__main__':
	unittest.main()

