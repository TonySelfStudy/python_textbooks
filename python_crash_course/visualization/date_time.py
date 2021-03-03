# Notes on learning how dates and times are used in python

# import datetime class from datetime module
from datetime import datetime



# get current date
datetime_object = datetime.now()
print(datetime_object)
print('Type :- ',type(datetime_object))

my_string = '2019-10-31'
my_string2 = ['2019-10-31', '2019-12-15']

# Create date object in given time format yyyy-mm-dd
my_date = datetime.strptime(my_string, "%Y-%m-%d")

print(my_date)
print('Type: ',type(my_date))

print('Month: ', my_date.month) # To Get month from date
print('Year: ', my_date.year) # To Get month from year