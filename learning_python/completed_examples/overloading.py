import random
from inspect import getsource

class employee:
    def __new__(cls):
        print("__new__ magic method is called")
        inst = object.__new__(cls)
        return inst

def __init__(self):
    print("__init__ magic method is called")
    self.name = 'Satya'


a = getsource(random.randint)
b = getsource(random.randrange)
