# Chap 38 of Learning Python
from inspectors import *
from sys import exc_info
insp = Inspector()


class Person:
    def __init__(self, my_name):
        self._name = my_name

    def get_name(self):
        print('... fetching from getName')
        return self._name

    def set_name(self, my_name):
        print('... setting from setName')
        self._name = my_name

    def del_name(self):
        print('... deleting from getName')
        del self._name

    name = property(get_name, set_name, del_name, "I'm a docstring for the name function")
    # print(name)
    # insp.climb_dir(name,None)

if False:
    try:
        print(Person.name.__doc__)
        x = Person('Bob')
        print(x.name)
        x.name = 'Sue'
        print(x.name)
        # del x.name
        # print(x.name)
    except Exception as exc:
        print(f"... In exception Handler ...")
        for i in exc_info():
            print(i)
        insp.climb_dir(exc_info()[2], None )
        print(f"\nEnd Exception")
        #stack_info()


class PropSquare:
    def __init__(self, base):
        self.base = base

    def set_base(self, base):
        self.base = base

    def get_base(self):
        return self.base ** 2

    x = property(get_base, set_base, )

if False:
    y = PropSquare(5)
    print(y.x)
    y.x = 10
    print(y.x)

class SimpleDecorator:

    def __init__(self):
        self.x = 3

    def cube_me(self):
        return self.x ** 3

    cube_me_print = cube_me

if False:
    y = SimpleDecorator()

    # z = y.cube_me
    # print(z)
    # print(z())

class Person:
    def __init__(self, my_name):
        print('... initializing in __init__')
        self._name = my_name

    def name(self):
        print('... fetching from getName')
        return self._name
    name = property(name)

    def set_name(self, my_name):
        print('... setting from setName')
        self._name = my_name
    name = name.setter(set_name)

    def del_name(self):
        print('... deleting from getName')
        del self._name
    name = name.deleter(del_name)

    # name = property(name, set_name, del_name, "I'm a docstring for the name function")
    # print(name)
    # insp.climb_dir(name,None)

if False:
        x = Person('Bob')
        print(x.name)
        x.name1 = 'Sue'
        print(x.name)
        print(Person.name.__doc__)
        del x.name
        # print(x.name)

class MyClass:
    y = 'class data'
    def __init__(self):
        print("In the __init__")
        self.x = "x set in __init__"
    def mygetter(self):
        """Gets the somewhat protected x variable"""
        print("In the mygetter")
        return self.x
    def mysetter(self, val):
        print("In the mysetter")
        self.x = val
    def mydeleter(self):
        print("In the mydeleter")
        del self.x
    z = property(mygetter, mysetter, mydeleter,)
    # insp(z, 'None')

if False:
    var1 = MyClass()
    print(var1.z)
    var1.z = "Reset in __main__ code"
    print(var1.z)
    del var1.z
    print(var1.z)


class Ager:
    def __init__(self):
        print("In the __init__")
        self._age = 10

    def age(self):
        print("In the getter")
        return self._age
    age = property(age)

    @age.setter
    def age(self, val):
        print("In the setter")
        self._age = val

    # insp(age, 'getter')

    @age.deleter
    def age(self):
        print("In the deleter")
        del self._age

if False:
    var1 = Ager()
    print(var1.age)
    var1.age = "Reset in __main__ code"
    print(var1.age)
    del var1.age
    print(var1.age)

if False:
    def decorator(f):
        def new_function():
            print("Extra Functionality")
            f()
        return new_function

    # @decorator
    def initial_function():
        print("Initial Functionality")
    initial_function = decorator(initial_function)

    initial_function()

if False:
    class Descriptor:
        def __get__(self, instance, owner):
            print("In Descriptor.__get__")
            print(f'self={self}\ninstance={instance}\nowner={owner}')
            print(f"instance.__class__ is owner is {instance.__class__ is owner}")
            return instance._age

        def __set__(self, instance, value):
            print("In Descriptor.__set__")
            instance._age = value
            return instance._age

        def __delete__(self, instance): pass

    class Person:
        age = Descriptor()

        def __init__(self, arg = "Initialized Age"):
            self._age = arg

    bob = Person(42)
    print(bob.age)
    bob.age = 21
    print(bob.age)

if False:
    class Descriptor:
        def __get__(self, instance, owner):
            print(self, instance, owner, sep='\n')
            return "__get__ return value"

    class Subject:
        attr = Descriptor()

    X = Subject()
    X.attr

    print(f"{'*'* 25}")
    print(f"{Subject.attr}")

if False:
    class D:
        def __get__(self, *args):
            print('get')
    class C:
        a = D()

    C.a
    x = C()
    x.a
    print(x.__dict__)
    print(C.__dict__)

    x.a = 10
    print(x.__dict__)
    print(C.__dict__)
    x.a

if False:
    class Person:
        def __init__(self, name="Default Name"):
            print('...initializing...')
            self._name = name

        class Descriptor:
            def __get__(self, instance, owner):
                print('...fetching...')
                return instance._name

            def __set__(self, instance, value):
                print('...setting...')
                instance._name = value

            def __delete__(self, instance):
                print('...deleting...')
                del instance._name
        name = Descriptor()

    bob = Person('Bob Smith')
    print(bob.name)
    bob.name = 'Robert Smith'
    print(bob.name)
    del bob.name
    # print(bob.name)

    print('-'*20)
    sue = Person()
    print(sue.name)
#    print(Person.name.__doc__)

if False:
    class SquareDescriptor:
        def __init__(self, value):
            self.value = value

        def __get__(self, instance, owner):
            print('...fetching square...')
            return self.value ** 2

        def __set__(self, instance, value):
            print('...setting...')
            self.value = value

        def __delete__(self, instance):
            print('...deleting...')
            del self.value

    class Client1:
        x = SquareDescriptor(3)

    class Client2:
        x = SquareDescriptor(32)

    c1 = Client1()
    c2 = Client1()
    c3 = Client2()

    print(c1.x)     # 3**2
    c1.x = 4
    print(c1.x)     # 4**2
    print(c2.x)     # 4**2
    print(c3.x)     # 32*2

    class SquareClient:
        def __get__(self, instance, owner):
            print('...fetching square...')
            return instance._value ** 2

        def __set__(self, instance, value):
            print('...setting...')
            instance._value = value

        def __delete__(self, instance):
            print('...deleting...')
            del instance._value

    class Client3:
        x = SquareClient()
        def __init__(self, value):
            self._value = value

    c4 = Client3(7)
    c5 = Client3(17)
    print(c4.x)
    print(c5.x)


if False:
    class DescState:
        def __init__(self, value):
            self.value = value
        def __get__(self, instance, owner):
            print('DescState get')
            return self.value * 10
        def __set__(self, instance, value):
            print('DescState set')
            self.value = value

    class CalcAttrs:
        X = DescState(2)
        Y = 3
        def __init__(self):
            self.Z = 4

    obj = CalcAttrs()
    print(obj.X, obj.Y, obj.Z)      # 20, 3, 4
    obj.X = 5                       # set to 5
    CalcAttrs.Y = 6                 # Y=6
    obj.Z = 7                       # Z = 7
    print(obj.X, obj.Y, obj.Z)      # 50, 6, 7

    obj2 = CalcAttrs()              # does not affect class level
    print(obj2.X, obj2.Y, obj2.Z)   # 50, 6, 4


if False:
    class DescBoth:
        def __init__(self, data):
            self.data = data
        def __get__(self, instance, owner):
            return f"{self.data}, {instance.data}"
        def __set__(self, instance, data):
            instance.data = data

    class Client:
        def __init__(self, data):
            self.data = data
        managed = DescBoth('spam')

    I = Client('eggs')
    I.managed
    I.managed = 'SPAM'
    I.managed

    print(I.__dict__)
    print(dir(I))

    a = [x for x in dir(I) if not x.startswith('__')]
    b = [x for x in dir(Client) if not x.startswith('__')]
    print(a)
    print(b)
    print(Client.__dict__)
    getattr(I, 'data')

if False:

    class Klass1:
        def __getattr__(self, name):
            print('... in __getattr__ ...')

        def __getattribute__(self, name):
            print('... in __getattribute__ ...')

        def __setattr__(self, name, value):
            print('... in __getattr__ ...')

        def __delattr__(self, name):
            print('... in __getattr__ ...')

    class Catcher:
        def __getattr__(self, name):
            print('... in __getattr__ ...')
            if name in self.__dict__:
                print(f"{name}={getattr(self, name)}")
            else:
                print(f"{name} is an unknown attribute")
            return

        def __setattr__(self, name, value):
            print('... in __setattr__ ...')
            self.__dict__[name] = value
            # setattr(self, name, value)

    obj1 = Catcher()
    obj1.job
    obj1.job = 10
    obj1.job
    print(obj1.__dict__)

if False:

    class Wrapper:
        def __init__(self, obj):
            self.wrapped = obj

        def __getattr__(self, attrname):
            print('In __getattr__: ' + attrname)
            y = getattr(self.wrapped, attrname)
            # insp(y,'None')
            return y

        # def __getattribute__(self, attrname):
        #     print('In __getattribute__: ' + attrname)
        #     tmp = object.__getattribute__(self, attrname)
        #     return tmp



    x = Wrapper([1, 2, 3])
    print(x)
    x.append(6)
    print(x.wrapped)
    #   print(x.append)

if False:
    class Animal:
        def __init__(self):
            self.name = 'General Animal'
        def speak(self):
            print('General Animal Sound')
        def move(self):
            print('General Animal Movement')
        def __getattr__(self, item):
            print("In Animal's __getattr__")
            print("A reference to undefined attribute was made")
            return print


    class Worm(Animal):
        def __init__(self):
            self.name = 'Worm'
        def __getattr__(self, item):
            print("In Worms's __getattr__")
            print("A reference to undefined attribute was made")
            return print

    class Dog(Animal):
        def __init__(self):
            self.name = 'Dog'
        def speak(self):
            print('Woof')
        def move(self):
            print('Walk')
        def __getattr__(self, item):
            print("In Dog's __getattr__")
            print("A reference to undefined attribute was made")
            return print

    mydog = Dog()
    mydog.speak()
    mydog.move()
    mydog.reproduce("This will be outputted by the returned print function")
    print('*'*50)

    myworm = Worm()
    myworm.speak()
    myworm.move()
    myworm.reproduce("This will be outputted by the returned print function")

if False:
    """Code to look into how intercepted methods and inheritance work out."""
    class Animal:
        def __init__(self):
            self.name = 'General Animal'
        def speak(self):
            print('General Animal Sound')
        def move(self):
            print('General Animal Movement')
        # def __getattribute__(self, item):
        #     print("In Animal's __getattribute__")
        #     print(f"A reference to attribute *{item}* was made and captured by the Animal class")
        #     base_class = object.__getattribute__(self, '__class__')
        #     print(f'My base class is: {base_class}')
        #     super_class = base_class.__bases__[0]
        #     print(f'My super class is: {super_class}')
        #     x1 = object.__getattribute__(self, item)  #Gets this self's item without recursion
        #     x1()
        #
        #     return print


    class Worm(Animal):
        def __init__(self):
            print("Creating a Worm")
            self.name = 'Worm'
        # def __getattr__(self, item):
        #     print(f"In Worms's __getattr__ because of reference to *{item}*")
        #     print("A reference to undefined attribute was made")
            return print

    class Dog(Animal):
        def __init__(self):
            print("Creating a Dog")
            self.name = 'Dog'
        def speak(self):
            print('Woof')
        def move(self):
            print('Walk')
        # def __getattribute__(self, item):
        #     print("In Dogs's __getattribute__")
        #     print(f"A reference to attribute *{item}* was made and captured by the Dog class")
        #     x1 = object.__getattribute__(self, item)  #Gets this self's item without recursion
        #     x1()
        #     print('*' * 50)
        #     x2 = super().__getattribute__(item)
        #     x2()
        #     print('*' * 50)
        #     x3 = getattr(super(), item)
        #     x3()
        #     return
        def __setattr__(self, key, value):
            print(self, key, value)
            # setattr(self, key, value)

            # self.__dict__[key] = value
            object.__setattr__(self, key, value)


    mydog = Dog()
    mydog.wag = 10
    print(mydog.__dict__)
    # mydog.speak()

    # mydog.move()
    # mydog.reproduce("This will be outputted by the returned print function")
    # print('*'*50)
    #
    # myworm = Worm()
    # myworm.speak()
    # myworm.move()
    # myworm.reproduce("This will be outputted by the returned print function")

if False:
    class Mammal(object):
        def __init__(self, mammalName):
            print(mammalName, 'is a warm-blooded animal.')


    class Dog(Mammal):
        def __init__(self):
            print('Dog has four legs.')
            Mammal.__init__(self, 'Dog')
#            super().__init__('Dog')


    d1 = Dog()

if False:
    class Person:
        def __init__(self, name):
            print(f'...In __init__ name=*{name}*')
            print(self.__dict__)

            self._name = name
            print('Leaving Init')

        # def __getattr__(self, attr):
        #     print(f'...In __getattr__ attr=*{attr}*')
        #     if attr == 'name':
        #         return self._name
        #     else:
        #         raise AttributeError
        def __getattribute__(self, attr):
            print(f'...In __getattribute__ attr=*{attr}*')
            if attr == 'name':
                attr = '_name'
            y = object.__getattribute__(self, attr)
            return y

        def __setattr__(self, attr, value):
            print(f'...In __setattr__ attr=*{attr}*, value=*{value}*')
            if attr == 'name':
                attr = '_name'
            self.__dict__[attr] = value

            # print(self.__doc__)
            # print(dir(self))
            # self.__class__

            # y = self.__dict__[attr]
            # dir(y)
            # # print(self.__dict__[attr])

        def __delattr__(self, attr):
            print(f'...In __delattr__ attr=*{attr}*')
            if attr == 'name':
                attr = '_name'
            else:
                raise AttributeError
            del self.__dict__[attr]

    bob = Person('Bob Smith')
    # print(bob.name)
    # bob.name = 'Robert Smith'
    # print(bob.name)
    # del bob.name
    #
    # print('-'*20)
    # sue = Person('Sue Jones')
    # print(sue.name)


if False:
    class Person:
        def __init__(self, name):
            print(f'...In __init__ name=*{name}*')
            self._name = name

        # def __getattr__(self, attr):
        #     print(f'...In __getattr__ attr=*{attr}*')
        #     if attr == 'name':
        #         return self._name
        #     else:
        #         raise AttributeError
        def __getattribute__(self, attr):
            print(f'...In __getattribute__ attr=*{attr}*')
            if attr == 'name':
                attr = '_name'
            y = object.__getattribute__(self, attr)
            return y

        def __setattr__(self, attr, value):
            print(f'...In __setattr__ attr=*{attr}*, value=*{value}*')
            if attr == 'name':
                attr = '_name'
            object.__setattr__(self, attr, value)
            # self.__dict__[attr] = value

        def __delattr__(self, attr):
            print(f'...In __delattr__ attr=*{attr}*')
            if attr == 'name':
                attr = '_name'
            else:
                raise AttributeError
            del self.__dict__[attr]

    bob = Person('Bob Smith')
    print(bob.name)
    bob.name = 'Robert Smith'
    print(bob.name)
    del bob.name

    print('-'*20)
    sue = Person('Sue Jones')
    print(sue.name)

if False:
    class AttrSquare:
        def __init__(self, value):
            self.value = value
        def __getattr__(self, attr):
            if attr == 'x':
                return self.value ** 2
            else:
                raise AttributeError
        def __setattr__(self, attr, value):
            # return object.__setattr__(self, attr, value)
            if attr == 'x':
                attr = 'value'
            self.__dict__[attr] = value


    y1 = AttrSquare(3)
    print(y1.x)
    y2 = AttrSquare(32)
    print(y2.x)


if False:
    class AttrSquare:
        def __init__(self, value):
            self.value = value

        def __getattribute__(self, attr):
            print(self, attr)
            if attr == 'x':
                attr = 'value'
            if attr == 'value':
                return object.__getattribute__(self, attr) ** 2
            else:
                raise AttributeError

        def __setattr__(self, attr, value):
            if attr == 'x':
                attr = 'value'
            print(self, attr, value)
            # self.__dict__[attr] = value
            object.__setattr__(self, attr, value)


    y1 = AttrSquare(3)
    print(y1.x)
    y2 = AttrSquare(32)
    print(y2.x)

if False:
    class fetcher:
        arg1 = 1
        def __init__(self, value):
            self.arg2 = value
        def __getattr__(self, item):
            if item == 'arg3':
                return "I'm arg3"
        def __setattr__(self, attr, value):
            # print(attr, value)
            if attr == 'arg3':
                print("You can't change arg3")
            else:
                object.__setattr__(self, attr, value)
        def __str__(self):
            # print("*", self.arg1, self.arg2, self.arg3, "*",)
            return ", ".join([str(self.arg1), str(self.arg2), str(self.arg3)])

    fetcher1 = fetcher(2)
    print(fetcher1)
    fetcher2 = fetcher(8)
    print(fetcher2)

if False:
    class fetcher:
        arg1 = 1
        def __init__(self, value):
            self.arg2 = value
        def __getattribute__(self, attr):
            if attr == 'arg3':
                return "I'm arg3"
            else:
                return object.__getattribute__(self, attr)

        def __setattr__(self, attr, value):
            # print(attr, value)
            if attr == 'arg3':
                print("You can't change arg3")
            else:
                object.__setattr__(self, attr, value)
        def __str__(self):
            # print("*", self.arg1, self.arg2, self.arg3, "*",)
            return ", ".join([str(self.arg1), str(self.arg2), str(self.arg3)])

    fetcher1 = fetcher(2)
    print(fetcher1)
    fetcher2 = fetcher(8)
    print(fetcher2)

# Page 1288, using Properties
if False:
    class Powers1:
        def __init__(self, square, cube):
            self._square = square
            self._cube = cube

        def set_square(self, square):
            self._square = square

        def get_square(self):
            return self._square ** 2

        def get_cube(self):
            return self._cube ** 3

        square = property(get_square, set_square)
        cube = property(get_cube)

    my_pow = Powers1(3, 4)
    print(my_pow)
    print(my_pow.square)
    print(my_pow.cube)
    my_pow.square = 5
    print(my_pow.square)

# Page 1289, using Descriptors
if False:
    class Square:
        def __get__(self, instance, owner):
            return instance._square  ** 2
        def __set__(self, instance, value):
            instance._square = value
    class Cube:
        def __get__(self, instance, owner):
            return instance._cube  ** 3
    class Powers2:
        square = Square()
        cube = Cube()
        def __init__(self, my_square, my_cube):
            self._square = my_square
            self._cube = my_cube

    my_pow = Powers2(3, 4)
    print(my_pow)
    print(my_pow.square)
    print(my_pow.cube)
    my_pow.square = 5
    print(my_pow.square)

# Page 1289, using __getattr__
if False:
    class Powers3:
        def __init__(self, my_square, my_cube):
            self._square = my_square
            self._cube = my_cube

        def __getattr__(self, item):
            if item == 'square':
                return self._square ** 2
            elif item == 'cube':
                return self._cube ** 3

        def __setattr__(self, key, value):
            if key == 'square': key = '_square'
            if key == 'cube': key = '_cube'

            if key == '_square':
                object.__setattr__(self, key, value)
            elif key == '_cube':
                object.__setattr__(self, key, value)

    my_pow = Powers3(3, 4)
    print(my_pow)
    print(my_pow.square)
    print(my_pow.cube)
    my_pow.square = 5
    print(my_pow.square)

# Page 1289, using __getattr__
if False:
    class Powers4:
        def __init__(self, my_square, my_cube):
            self._square = my_square
            self._cube = my_cube

        def __getattribute__(self, item):
            if item == 'square':
                return object.__getattribute__(self, '_square') ** 2
            elif item == 'cube':
                return object.__getattribute__(self, '_cube') ** 3

        def __setattr__(self, key, value):
            if key == 'square': key = '_square'
            if key == 'cube': key = '_cube'

            if key == '_square':
                object.__setattr__(self, key, value)
            elif key == '_cube':
                object.__setattr__(self, key, value)

    my_pow = Powers4(3, 4)
    print(my_pow)
    print(my_pow.square)
    print(my_pow.cube)
    my_pow.square = 5
    print(my_pow.square)

# Page 1292
if False:
    class GetAttr:
        eggs = 88
        def __init__(self):
            self.spam = 77
        def __len__(self):
            print('__len__ : 42')
            return 42
        def __getattr__(self, item):
            print('getattr: ' + item)
            if item == '__str__':
                return 'lamda function 1'
            else:
                return 'lamda function 2'

    x = GetAttr()
    print(x.eggs)
    x.eggs = 99
    print(x.eggs)
    y = GetAttr()
    print(y.eggs)

    print(x.spam)
    x.other
    len(x)

# Page 1300
if True:
    class CardHolder:
        acctlen = 8
        retireage = 59.5

        def __init__(self, acct, name, age, addr):
            self.acct = acct
            self.name = name
            self.age = age
            self.addr = addr

        def getName(self):
            return self._name
        def setName(self, value):
            value = value.lower().replace(' ', '_')
            self._name = value
        name = property(getName, setName)

        




