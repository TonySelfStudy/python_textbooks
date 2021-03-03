# Learning Python Chap 39 Decorator Code
# I found how function, methods, and decorators interact to be a bit confusing
# I created some test cases to walk though usage.
# Pay close attention being paid to when 'self' arguments are automatically passed.

from inspectors import Inspector
insp = Inspector()

if True:
    """Functions, classes, and decorators to explore how python works under-the-hood"""

    def func01(x, y=-10):
        """Simple function not associated with a class"""
        return x * y

    def deco_func(f):
        """A function decorator not associated with a specific class"""
        print(f'In deco_func.  f: {f}')
        def return_func(*args):
            print(f"In deco_func's return_func.  f: {f}.  Args: {args}.  Will return: ", end='')
            a = f(*args)
            print(a)
            return a
        return return_func

    class deco_class:
        """A class that will have some attributes affected by a decorator"""
        print(f'In deco_class.')
        def __init__(self, f):
            self.name = 'deco_class'
            self.f = f
            print(f'in deco_class __init__.  type(f): {type(f)}')

        def __call__(self, *args, **kwargs):
            return self.f(*args, **kwargs)

    class C:
        """Test class to examine how its methods can be affected by decorators."""
        def __init__(self):
            self.func05 = deco_func(func01)
            #   self.func05 is an instance variable created by a function decorating a function

            self.func06 = deco_func(C.meth01)
            #   self.func06 is an instance variable created by a function decorating
            #       a method referenced by its class.
            #   Even though it was created by decorating a method, it is still a simple function
            #       so it has type <'function'> not <'method'>
            #   When you call func06, it will not receive the implicit self argument.
            #   If you want func06 to receive a 'self' argument, it must be passed explicitly

            self.func07 = deco_func(self.meth01)
            #   self.func07 is an instance variable created by a function decorating
            #       a method referenced by an instance of the class.
            #   func07 is a bound method so when it is invoked elsewhere (e.g. in a decorator),
            #       'self.meth01' will retain a reference to its object instance
            #       that can be passed subsequently to other methods.
            #   For example:
            #       a = self.meth01
            #       a(x,y)  will actually be called as C.meth01(a, x, y)
            #   In effect, the decorator will work as expected without mismapping on subsequent method calls

            self.class03 = deco_class(func01)
            #   self.class03 is an instance variable created by a class decorating a function

            self.class04 = deco_class(self.meth01)
            #   self.class04 is an instance variable created by a class decorating
            #       a method referenced by an instance of the class.


        def meth01(self, x, y=-99):
            """Bound Class Method"""
            return x + y

        func03 = deco_func(func01)
        #   func03 is a method that is created by decorating a *regular function*
        #   Calling this method directly through the class will not
        #       implicitly pass a 'self' as the 1st argument,
        #       which will result in a compatible signature and work as expected
        #   Invoking this function through a object instance will
        #       implicitly pass a 'self' as the 1st argument,
        #       which will result in a incompatible signature and not work as expected.
        #   Calling through the instance will have 1 too many arguments
        #       and likely crash the underlying function or not work as expected

        func04 = deco_func(meth01)
        #   func04 is a class level attribute
        #   It is a method that was created by decorating a method
        #   You can call this method directly through the class name eg, C.func04(...)
        #       and explicitly include a 'self' object instance
        #   If you call this function through an object instance
        #       a 'self' object instance will automatically be included in the argument list

        class01 = deco_class(func01)
        #   A class level attribute that simulates a decorated function.
        #   class01 nor func01 are methods.
        #       class01 a class level instance of type 'deco_class'
        #       func01 is a function (not a method)
        #   class01 'simulates' a function by using deco_class's __call__ method.
        #   Since class01 is not a method, it will not receive an implicit
        #       object instance of 'Class C self' in its argument list when called.
        #   As such, class01 should only be used with functions and it
        #       will likely fail when used for method's that expect 'self' in the signature

        class02 = deco_class(meth01)
        #   A class level attribute that simulates a decorated method.
        #       class02 is a class level instance of type 'deco_class'
        #       meth01 is a method and will expect a 'self' argument passed
        #   Since class01 is not a method, it will not receive an implicit
        #       object instance of 'Class C self' in its argument list when called.
        #   meth01 expect's 'self' to be passed, so this implementation will likely fail


    # --------------------------------------------------------------------------
    # Example 01. Function decorated by function decorator.  No classes involved.
    #             Works: all cases.
    # --------------------------------------------------------------------------
    print('\n', '1' * 50)
    print(f"func01's type: {type(func01)}")
    func08 = deco_func(func01)
    print(f"func07's type: {type(func08)}")
    print(func08(3, 5))  # Returns 15 as expected

    # --------------------------------------------------------------------------
    # Example 02. Class method called directly and through an instance variable.
    #             No decorators used.
    #             Works: all cases.
    # --------------------------------------------------------------------------
    print('\n', '2'* 50)
    c2 = C()
    print(f"meth01's type: {type(c2.meth01)}")
    print(c2.meth01(7, 11))
    #   Undecorated method works as expected and returns 18
    
    # --------------------------------------------------------------------------
    # Example 03. Class attribute method created by a function decorating a regular function.
    #             Works: when accessing through class name.
    #             Fails: when accessing through object instance access.
    # --------------------------------------------------------------------------
    print('\n', '3' * 50)
    c3 = C()
    print(f"func03's type: {type(c3.func03)}")
    print(C.func03(2, 3))
    #   Returns 6.  No object instances passed, so no 'self' argument mismatches

    try:
        print(c3.func03(5, 7))
        #   Want it to return 35, but it fails because implicit self argument included
        #   throws exception for argument mismatch
    except Exception as e:
        print('\nXXX Expected error captured XXX')
        print(e)

    # --------------------------------------------------------------------------
    # Example 04. Class attribute method created by a function decorating a class method.
    #             Works:  when accessing through object instance access.
    #                     when accessing through class name if you first include an object instance.
    #             Fails:  when accessing through class name without object instance.
    # --------------------------------------------------------------------------
    print('\n', '4' * 50)
    c4 = C()
    print(f"func04's type: {type(c4.func04)}")
    print(c4.func04(8, 12))
    #   Return 20 as expected
    #   func04 is a method that was created by decorating a method
    #   Calling func04 by an object instance implicitly includes a 'self' as the 1st argument
    #   As a result, the methods will have compatible signatures and will work as expected

    print(C.func04(2, 4))
    #   Want it to return 6, but it returns -96
    #   Calling func04 through the class name (not through an object instance)
    #       will not include a 'self' object instance
    #   Since the func04 expects self as the 1st argument,
    #       you have an incompatible signature with one less parameter than expected
    #   This invocation will usually fail, but does not cause an exception here
    #       because the parameter list has a default member
    #   The self argument will be mismapped and the function will not work as expected

    print(C.func04(c4, 3, 5))
    #   You can call by class name, but only if you pass an instance of an object as first method

    # --------------------------------------------------------------------------
    # Example 05. Object instance attribute created by a function decorating a function.
    #             Works: when accessing through object instance.
    #             Fails: NA
    # --------------------------------------------------------------------------
    print('\n', '5' * 50)
    c5 = C()
    print(f"func05's type: {type(c5.func05)}")
    print(c5.func05(3, 9))
        # Results in 27 as expected.  Since there are no 'selfs' being passed to the instance variable,
        #   and func1 is a simple function without self's, everything works fine.

    # --------------------------------------------------------------------------
    # Example 06. Object instance attribute created by a function decorating
    #               one of its class methods.
    #             Works:  when accessing through object instance if you first include an object instance as an argument.
    #             Fails:  otherwise
    # --------------------------------------------------------------------------
    print('\n', '6' * 50)
    c6 = C()
    print(f"func06's type: {type(c6.func06)}")
    print(c6.func06(13, 17))
    #   Want it to return 30, but returns -82
    #   meth01 is a method
    #   func06 is an object instance variable that references a function
    #   Since func06 is defined at the object instance level, not the class level,
    #       it is a regular function and calling it does not implicitly pass the self argument
    #       so underlying method will receive one less parameter than expected

    print(c6.func06(c2, 23, 27))
    #   Returns 50 as expected
    #   meth01 is a method, func06 is a function
    #   You can explicitly include a reference to the calling object
    #       which will allow the function to call the method with the explicitly passed 'self' argument

    # --------------------------------------------------------------------------
    # Example 07. Object instance attribute created by a function decorating
    #               a bound method of its class.
    #             Works:  If you pass the arguments normally without an explicit 'self' being passed.
    #                     Note, an implicit self is not passed below either.
    # --------------------------------------------------------------------------
    print('\n', '7' * 50)
    c7 = C()
    print(f"func07's type: {type(c7.func07)}")
    print(c7.func07(3, 7))
    #  Returns 10 as expected.  Since the decorator used a bound function,
    #   the 'self' information of the object instance is retained and there is no argument mismapping

    # --------------------------------------------------------------------------
    # Example 08. Class attribute method created by a class decorating a function.
    #             Works:  As expected, no implicit self is passed, and no self is required
    # --------------------------------------------------------------------------
    print('\n', '8' * 50)
    c8 = C()
    print(f"class01's type from C: {type(C.class01)}")
    print(C.class01(4, 8))
    # returns 32 as expected. No 'self' argument is passed, not expected

    # --------------------------------------------------------------------------
    # Example 09. Class attribute method created by a class decorator
    #               modifying a method
    #             Fails: accessing the variable without explicitly including a self object as the 1st argument
    # --------------------------------------------------------------------------
    # Class attribute variable created by a decorating class of a method function
    print('\n', '9' * 50)
    c9 = C()
    print(f"class02's type from C: {type(C.class02)}")
    print(C.class02(4, 8))
    #   Want 12, but will get -91
    #   A 'self' argument is not passed to class02
    #       but will be expected by its underlying meth01
    #   There is an argument signature mismatch and arguments will be mismapped

    # --------------------------------------------------------------------------
    # Example 10. Object instance attribute created by a class decorating a regular function.
    #             Works:  As expected, no implicit self is passed, and no self is required
    # --------------------------------------------------------------------------
    # Object instance variable created by a decorating class of a regular function
    print('\n', '10' * 25)
    c10 = C()
    print(f"class03's type from c6: {type(c10.class03)}")
    print(c10.class03(3, 7))
    #   returns 21 as expected. No 'self' argument is passed, not expected

    # --------------------------------------------------------------------------
    # Example 11. Object instance attribute created by a class decorating
    #               a bound method of its class.
    #             Works:  If you pass the arguments normally without an explicit 'self' being passed.
    #                     Note, an implicit self is not passed below either.
    # --------------------------------------------------------------------------
    print('\n', '11' * 25)
    c11 = C()
    print(f"class04's type from c8: {type(c11.class04)}")
    print(c11.class04(6, 7))
    #   Receives 13 as expected.
    #   A 'self' argument is not passed to class04 in this call,
    #       but in the __init__, class04 was bound to its object instance
    #   When the decorator calls this method, the bound method will retain the self info
    #       and there will be no mis-mapping of argument
