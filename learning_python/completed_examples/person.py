from classtools import AttrDisplay

class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    # def __repr__(self):
    #     return f'Person: {self.name}, {self.pay}'


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self, (percent + bonus))

    # def __repr__(self):
    #     return f'Manager: {self.name}, {self.pay}'


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    tom = Manager('Tom Jones', 100000)

    for obj in (bob, sue, tom):
        print(f"Before Raise: {obj}")
        obj.giveRaise(0.10)
        print(f"After Raise: {obj}")
