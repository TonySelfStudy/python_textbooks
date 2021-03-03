from person import Person, Manager

bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager('Tom Jones', 100000)

team = [bob, sue, tom]
print(team)

import shelve
db = shelve.open('persondb')
for obj in team:
    db[obj.name] = obj
db.close

