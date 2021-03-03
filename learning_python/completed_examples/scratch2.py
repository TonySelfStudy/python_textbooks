from tony_utilites import my_calling_statement as mcs
from tony_utilites import full_stack as fs

if True:
    class Super:
        def hello(self):
            self.data = 'spam'

    class Sub(Super):
        def hola(self):
            self.data2 = 'eggs'

    def print_dict(obj):
        #    print(f"Inspecting: {obj.__name__}")
        my_dict = obj.__dict__

        print('*'*50)
        # mcs()
        fs()
        for k, v in my_dict.items():
            print(f'{k}: {v}')
        print('-'*50)


if True:
    x = Super()
    y = Sub()
    print_dict(Super)
    print_dict(Sub)
    print_dict(x)
    print_dict(y)

    y.hello()
    y.hola()

    print_dict(x)
    print_dict(y)


if False:
    a = dir()
    print(type(a))

    b = __name__
    print(type(b), b)

    for i in a:
        print(i)
        print(f"     {eval(i)}")

    print(dir())

    c = globals().copy()
    print(c)
    for k, v in c.items():
        print(f'{k}: {v}')


if False:
    x = Sub()
    print(x.__dict__)
    print(x.__class__)
    print(x.__class__.__bases__)
    print(Super.__bases__)
    print(Super.__bases__[0].__bases__)
    print(object)
    print(object.__base__)


if False:
    class Number:
        def __init__(self, base):
            self.base = base

        def double(self):
            return self.base * 2

        def triple(self):
            return self.base * 3


    x = Number(2)  # Class instance objects
    y = Number(3)  # State + methods
    z = Number(4)
    print(x.double())  # Normal immediate calls

    acts = [x.double, y.double, y.triple, z.double]  # List of bound methods
    for act in acts:  # Calls are deferred
        print(act())  # Call as though functions

    bound = x.double
    print(bound.__self__, bound.__func__)

    print(bound.__self__.base)
    print(bound())
