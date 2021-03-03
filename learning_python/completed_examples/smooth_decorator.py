# Learning Python Chap 39 Decorator Code
# I found how function, method's, decorators to be a bit confusing
# I created some test cases to walk though how functions, methods, decorators interact
#   with close attention being paid to when 'self' arguments are automatically passed

from inspectors import Inspector
insp = Inspector()

if True:
    """Functions, classes, and decorators to explore how python works under-the-hood"""

    def func1(x, y=-10):
        """Simple function not associated with a class"""
        return x * y

    def deco1(f):
        """A function decorator not associated with a specific class"""
        print(f'In deco1.  f: {f}')
        def return_func(*args):
            print(f"In deco1's return_func.  f: {f}")
            print(*args)
            return f(*args)
        return return_func

    class deco2:
        """A class that will have some attributes affected by a decorator"""
        print(f'In deco2.')
        def __init__(self, f):
            self.name = 'deco2'
            self.f = f
            print(f'in deco2 __init__')
            print(f'type(f): {type(f)}')

        def __call__(self, *args, **kwargs):
            return self.f(*args, **kwargs)

    class C:
        def __init__(self):
            self.name = 'C'
            self.func4 = deco1(C.func2)  # self.func4 is an instance variable pointing to a simple function (not a method).
                                         # Even though it was created by decorating a method, it is still a simple function
                                         # so it has type <'function'> not <'method'>
                                         # When you use it in a function call, it will not receive the implicit self
                                         # If you want func4 to have a 'self' reference to pass to it underlying method
                                         #  it will have to be included explicitly as the first func4 argument
            self.classy_func2 = deco2(func1)        # An object instance class simulating a decorated function
            self.classy_func4 = deco2(self.func2)   # An object instance class simulating a decorated method
                                                    # self.func2 is a bound method, when it is invoked in the
                                                    # decorator, it will be done as C.func2(self, args)
                                                    # So the decorator will receive the self argument first and work as expected

        def func2(self, x, y=-99):
            """Bound Class Method"""
            return x + y

        func5 = deco1(func2)            # func5 is a class level attribute
                                        # It is a method that was created by decorating a method
                                        # You can call this method directly through the class name eg, C.func5(...)
                                        #   and explicitly include a 'self' object instance
                                        # If you call this function through an object instance
                                        #   a 'self' object instance will automatically be included in the argument list

        func6 = deco1(func1)            # func6 is a method that is created by decorating a *regular function*
                                        # Calling this method directly through the class will not
                                        #   implicitly pass a 'self' as the 1st argument,
                                        #   which will result in a compatible signature and work as expected

                                        # Invoking this function through a object instance will
                                        #   implicitly pass a 'self' as the 1st argument,
                                        #   which will result in a incompatible signature and not work as expected.
                                        # Calling through the instance will have 1 too many arguments
                                        #   and likely crash the underlying function or not work as expected

        classy_func1 = deco2(func1)     # A class level attribute that simulates a decorated function.
                                            # classy_func1 nor func1 are methods.
                                            #   classy_func1 a class level instance of type 'deco2'
                                            #   func1 is a function (not a method)
                                            # classy_func1 simulates a function by using deco2's __call__ method.
                                            # Since classy_func1 is not a method, it will not receive an implicit
                                            #   object instance of 'Class C self' in its argument list when called.
                                            # As such, classy_func1 should only be used with functions and
                                            #   will likely fail when used for method's that expect 'self' in the signature

        classy_func3 = deco2(func2)     # A class level attribute that simulates a decorated method.
                                            #   classy_func3 a class level instance of type 'deco2'
                                            #   func2 is a method and will expect a 'self' argument passed
                                            # Since classy_func1 is not a method, it will not receive an implicit
                                            #   object instance of 'Class C self' in its argument list when called.
                                            # func2 expect's 'self' to be passed, so this implementation will likely fail


    # Show that the function implementation works for both functions and methods
    # --------------------------------------------------------------------------

    # Simple function, and decorated simple function
    print('1' * 50)
    print(f"func1's type: {type(func1)}")
    func3 = deco1(func1)
    print(f"func3's type: {type(func3)}")
    print(func3(3, 5))  # Returns 15 as expected

    # Class method called directly and through an instance variable that is a decorated version of the method
    print('2'* 50)
    c2 = C()
    print(f"func2's type: {type(c2.func2)}")
    print(c2.func2(7, 11))      # Undecorated method works as expected and returns 18
    print(f"func4's type: {type(c2.func4)}")
    print(c2.func4(13, 17))     # Want it to return 30, but returns -82
                                # func2 is a method
                                # func4 is an object instance variable that references a function
                                # Since func4 is defined at the object instance level, not the class level,
                                # it is a regular function and calling it does not implicitly pass the self argument
                                # The underlying method will receive one less parameter than expected

    print(c2.func4(c2, 23, 27))   # Returns 50 as expected
                                # func2 is a method, func4 is a function
                                # You can explicitly include a reference to the calling object
                                # which will allow the function to call the method with the explicitly passed self

    # Class attribute pointing to a decorated class method
    print('3' * 50)
    c3 = C()
    print(f"func5's type: {type(c3.func5)}")
    print(c3.func5(8, 12))  # Want it to return 20, and it does
                            # func5 is a method that was created by decorating a method
                            # Calling func5 by an object instance implicitly includes a 'self' as the 1st argument
                            # As a result, the methods will have compatible signatures and will work as expected
    print(C.func5(2, 4))    # Want it to return 6, but it returns -96
                            # Calling func5 through the class name (not through an object instance)
                            #   will not include a 'self' object instance
                            # Since the func5 expects self as the 1st argument,
                            #   you have an incompatible signature with one less parameter than expected
                            # This invocation will usually fail, but does not cause an exception here
                            #   because the parameter list has a default member
                            # The self argument will be mismapped and the function will not work as expected

    # Class attribute method created by decorating a regular function
    print('4' * 50)
    c4 = C()
    print(f"func6's type: {type(c4.func6)}")
    print(C.func6(2, 3))        # Want it to return 6, and it does since no self instances could be passed
    # print(c4.func6(5, 7))     # Want it to return 35,
                                #   but it fails because implicit self argument included

    # Class attribute variable created by a decorating class of a regular function
    print('5' * 50)
    c5 = C()
    print(f"classy_func1's type from C: {type(C.classy_func1)}")
    print(C.classy_func1(4, 8))     # returns 32 as expected.
                                    # No 'self' argument is passed, not expected

    # Object instance variable created by a decorating class of a regular function
    print('6' * 50)
    c6 = C()
    print(f"classy_func2's type from c6: {type(c6.classy_func2)}")
    print(c6.classy_func2(3, 7))    # returns 21 as expected.
                                    # No 'self' argument is passed, not expected

    # Class attribute variable created by a decorating class of a method function
    print('7' * 50)
    c7 = C()
    print(f"classy_func3's type from C: {type(C.classy_func3)}")
    print(C.classy_func3(4, 8))     # Want 12, but will get -91
                                    # A 'self' argument is not passed to classy_func3
                                    #   but will be expected by its underlying func2
                                    # There is an argument signature mismatch and arguments will be mismapped

    # Object instance variable created by a decorating class of a method
    print('8' * 50)
    c8 = C()
    print(f"classy_func4's type from c8: {type(c8.classy_func4)}")
    print(c8.classy_func4(6, 7))    # want and receive 13.
                                    # A 'self' argument is not passed to classy_func4 in this call,
                                    #   but in the __init__, classy_func4 was bound to its object instance
                                    # When the decorator calls this method, the bound method will retain the self info
                                    #   and there will be no mismapping of argument

#########################
# Scratch code below #
#########################

if False:
    def deco2(func):
        func.decoed = True
        return func

    def deco3(func):
        def wrapper(*args):
            print('inside the wrapper')
            print('adding 1 to each of the arguments')
            args = [i+1 for i in args]
            print(f'The args are: {args}')
            return func(*args)
        return wrapper

    class deco4():
        def __init__(self, func):
            self.func = func
        def __call__(self, *args):
            print('In the class __call__')
            args = [i+10 for i in args]
            return self.func(*args)

    def func1(x, y):
        print(f'x={x}, y={y}, x+y={x+y}')
        return x+y

    @deco2
    def func2(x, y):
        print(f'x={x}, y={y}, x+y={x+y}')
        return x+y

    @deco3
    def func3(x, y):
        print(f'x={x}, y={y}, x+y={x+y}')
        return x+y

    @deco4
    def func4(x, y):
        print(f'x={x}, y={y}, x+y={x+y}')
        return x+y

    # a = func1(1, 3)
    # print(a)
    # print(dir(func1))
    #
    # b = func2(5, 7)
    # print(b)
    # print(dir(func2))
    #
    # c = func3(11, 13)
    # print(c)
    # print(dir(func3))

    d = func4(17, 23)
    print(d)
    print(dir(func4))

if False:
    def func_outer(*args):
        print(f"Outer function args: {args}")
        outer_args = args
        def func_inner(*args):
            print(f"   Inner function args: {args}")
            print(f"      Can still see outer_args: {outer_args}")
        return func_inner

    a = func_outer(1, 2, 3, 4)
    a(5, 6)

    b = func_outer
    b(5, 6)(10, 20)

if False:
    def deco1(f):
        print("I'm in deco1")
        print(f"deco1 args: {f}")
        def effed(*args):
            print("I'm starting effed")
            print(f"effed args: {args}")
            effed.decoed = 'not sure whats up'          # Not sure how func1 sees this, maybe it is bad form to have the decorated function use variables from the decorator?
            f('a', 'b', 'c')
            print("I'm leaving effed")
        return effed

    def func1(*args):
        print("I'm in func1")
        print(f"func1 args: {args}")
        print(func1.decoed)

    print('*'*20)
    func1 = deco1(func1)
    print('-'*20)
    func1(1, 2, 3)

if False:
    def deco1(f):
        print(f'In deco1.  args: {f}')
        def return_func(*args):
            print(f'In return_func.  args: {args}')
            print(f'calling original function.')
            a = f(*args)
            print(f'completed original function.')
            return a
        return return_func

    def func1(x, y):
        print(f'In func1.  args: x={x} y={y}')
        print(f'I return their sum which is {x+y}')
        return x + y

    @deco1
    def func3(x, y):
        print(f'In func3.  args: x={x} y={y}')
        print(f'I return their sum which is {x+y}')
        return x + y


    print('*'*30)
    func2 = deco1(func1)
    print('*'*30)
    a = func1(1, 3)
    print('*'*30)
    b = func2(5, 7)
    print('*'*30)
    c = func2(11, 13)
    print(a, b, c)

if False:
    class deco_class:
        def __init__(self, f):
            print('In the __init__')
            self.f = f
        def __call__(self, *args, **kwargs):
            print('In the __call__')
            return self.f(*args)

    def func1(x, y):
        print(f'In func1.  args: x={x} y={y}')
        print(f'I return their sum which is {x+y}')
        return x + y

    func2 = deco_class(func1)
    print(func2(1, 3))

if False:
    # Show that using a bound method fails when using class decoration
    # Actually, since I include a default method, it does not crash it just does the wrong thing
    class deco_class:
        def __init__(self, f):
            print('In the __init__')
            print(f'self: {self}')
            self.f = f
        def __call__(self, *args, **kwargs):
            print('In the __call__')
            print(f'self: {self}')
            print(f'args: {args}')

            return self.f(*args)

    def func1(x, y):
        print(f'In func1.  args: x={x} y={y}')
        print(f'I return their sum which is {x+y}')
        return x + y

    class C:
        def func2(self, x, y=-99):
            print(f'In func2.  args: self={self} x={x} y={y}')
            print(f'I return their sum which is {x + y}')
            return x + y
        func3 = deco_class(func2)
        print(dir(func2))
        print(dir(func3))
        print(func2)
        print(func3)


    print('1'*30)
    my_c = C()
    print('2'*30)
    print(my_c.func3(11, 13))
    print('3'*30)
    print(C.func2(my_c, 15, 17))
    print('4'*30)
    print(C.func3(my_c, 23, 27))
    print('5' * 30)
    print(C.func2)
    print(dir(C.func2))
    print('6' * 30)
    insp.climb_dir(C.func2, None)
    print('7' * 30)
    insp.climb_dir(C.func3, None)

if False:
    def deco1(f):
        print(f'In deco1.  args: {f}')
        def return_func(*args):
            print(f'In return_func.  args: {args}')
            print(f'calling original function.')
            a = f(*args)
            print(f'completed original function.')
            return a
        return return_func

    class C:
        def func2(self, x, y=-99):
            print(f'In func2.  args: self={self} x={x} y={y}')
            print(f'I return their sum which is {x + y}')
            return x + y
        func3 = deco1(func2)
        print(deco1)
        print(func2)
        print(func3)

    print('1'*30)
    my_c = C()
    print('2'*30)
    print(my_c.func3(11, 13))
    print('3'*30)
    print(my_c.func3)
if False:
    class IClass:
        def __init__(self):
            print('in IClass init')
            self.ivar = abs
        def __call__(self, *args, **kwargs):
            print(f'In my_abs.  args: self={self} args={args}')
            return self.ivar(*args)


    class Passer:
        """See how self is passed to methods and functions in a class"""
        ic = IClass()
        def __init__(self):
            self.x = 'in Passer init'
            self.ivar = abs       # Have an instance variable have a reference to a function

        def my_abs(self, val):            # my_abs is a method ... so it will implicitly be passed a self when called
            print(f'In my_abs.  args: self={self} args={val}')
            return abs(val)

    x = Passer()
    print(x.ivar(-10))
    print(x.my_abs(-15))
    print(Passer.my_abs(x, -17))
    print(x.ic.__call__(-21))
    print(x.ic(-22))
    print(getattr(x, 'ic')(-25))
    print(Passer.ic(x, -99))