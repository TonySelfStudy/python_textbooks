# Programming Pandas Example 1-21
import shelve

shelve_name = 'class-shelve'

class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def __repr__(self):
        return f'{self.lastName()}, {self.firstName()}; age: {self.age}; pay: {self.pay}; job: {self.job}'

    def lastName(self):
        return self.name.split()[-1]

    def firstName(self):
        return self.name.split()[0]

# Load into shelve
if False:
    bob = Person('Bob Smith', 42, 30000, 'software')
    sue = Person('Sue Jones', 45, 40000, 'hardware')
    tom = Person('Tom Doe', 50, 50000, 'manager')

    db = shelve.open(shelve_name)
    db['bob'] = bob
    db['sue'] = sue
    db['tom'] = tom
    db.close()

if False:
    db = shelve.open(shelve_name)
    for k, v in db.items():
        print(f'key: {k}\t\tvalue: {v}')
    db.close()


if True:
    fieldnames = ('name', 'age', 'job', 'pay')
    maxfield = max(len(f) for f in fieldnames)

    db = shelve.open(shelve_name)

    while True:
        key = input('\nKey? => ')
        print(f'Processing: {key}')
        if not key: break
        try:
            record = db[key]
        except:
            print(f'No such key {key} in {db}')
        else:
            for field in fieldnames:
                print(f'{field}: {getattr(record, field)}')
