# Scratch code to learn about decorating classes
from inspectors import Inspector
insp = Inspector()
import plotly.graph_objects as go
import plotly.io as pio


if False:
    """1st try to learn class decoration basics.
    This version will create a DecoClass instance for each class type it receives,
    but it will not store multiple instances of the same type.
    Remember, if you create the object in the __call__ then you won't have a unique object for each instance.
    To make each instance unique, it has to be created in the __init__"""

    class DecoClass:
        def __init__(self, cls):
            self.cls = cls                      # Save original class on decoration
        def __call__(self, *args, **kwargs):    # Called on instantiation
            self.wrapped = self.cls(*args, **kwargs)
            print(f"In the __call__, self: {self}, self.wrapped: {self.wrapped}")
            return self.wrapped
        def __getattr__(self, item):            # get attribute from underlying class
            tmp = getattr(self.wrapped, item)
            return tmp
    class C:                        # C will be manually decorated
        def __init__(self, x, y):
            self.attr = 'spam'
    @DecoClass
    class D:                        # D is automatically decorated
        def __init__(self, x, y):
            self.attr = 'spam'

    print(DecoClass)
    E = DecoClass(C)
    print(E)
    e1 = E(6, 7)
    print(e1)
    e2 = E(11, 13)
    print(e1)
    print(e2)

    # d1 = D(6, 7)
    # print(d1)
    # print(d1.attr)
    # d2 = D(6, 7)
    # print(d1)
    # print(d2)

if False:
    """Creates a new wrapper for every instance (since it is created in the init)"""
    def deco_func(cls):
        class Wrapper:
            def __init__(self, *args, **kwargs):
                self.obj = cls(*args, **kwargs)
            def __getattr__(self, item):
                return getattr(self.obj, item)
        return Wrapper

    class C:                        # C will be manually decorated
        def __init__(self, x, y):
            self.attr = 'spam'
    @deco_func
    class D:                        # D is automatically decorated
        def __init__(self, x, y):
            self.attr = 'spam'

    print(deco_func)
    E = deco_func(C)
    print(E)
    e1 = E(6, 7)
    print(e1)
    e2 = E(11, 13)
    print(e1)
    print(e2)
    print(e2.attr)

    def func2(x): return lambda y: x + abs(y)

    a = func2(5)
    print(a(-6))


if False:
    def func01(): return 'base'

    """look into nested decorations"""
    def a(f):
        return lambda : 'x' + f()
    def b(f):
        return lambda : 'y' + f()
    def c(f):
        # print('in c')
        return lambda : 'z' + f()

    # c = a(b(c(func01)))
    # print(c())

    def func02(): return 'base'

    d = a(b(c(func02)))
    print(d())

    @a
    @b
    @c
    def func03(): return 'base'

    print(func03())


if False:
    """Learning decorators with arguments

    @decorator(A, B)
    def func01(args)

    is treated as
    decorator(A,B)(func01)(args)

    1st decorator (A,B) is called which returns a callable
    2nd that callable is invoked with the func01 as an argument returning a callable
    3rd the second callable is invoked with argument args

    """

    def deco_with_args(A, B):
        print(f'Do something with {A}, {B}')
        def real_decorator(f):
            print(f'Decorating function f, turning it to min')
            return min
        return real_decorator

    def func01(*args):
        print(f'in func01 called with args: {args}')
        return max(*args)

    a = 'arg1'
    b = 'arg2'

    func02 =  deco_with_args(a, b)(func01)

    print(func01(1, 2, 99, 4))
    print(func02(1, 2, 99, 4))


if False:
    """implement tracer approach from page 1328"""

    class Tracer:
        def __init__(self, f):
            self.func = f
            self.calls = 0
        def __call__(self, *args, **kwargs):
            self.calls +=1
            print(f'Making call {self.calls} to func: {self.func} with args: {args}')
            return self.func(*args, **kwargs)

    def func01(a, b, c):
        print(a, b, c)

    # explicitly rebind function
    x = Tracer(func01)  # calls Tracer.__init__ returns a Tracer instance
    x(1, 2, 3)          # calls Tracer.__call__(x, 1, 2, 3)
    x(4, 5, 6)
    x(7, 8, 9)

    # rebind with decorator
    @Tracer
    def func02(a, b, c):
        print(a, b, c)

    func02(10, 11, 12)
    func02(13, 14, 15)
    func02(16, 17, 18)


if False:
    """Practice decorators based on page 1340"""
    import time
    import sys
    print(sys.version_info)

    class timer:
        def __init__(self, func):
            self.func = func
            self.alltime = 0
        def __call__(self, *args, **kargs):
            start = time.process_time()
            result = self.func(*args, **kargs)
            elapsed = time.process_time() - start
            self.alltime += elapsed
            print(f"{self.func.__name__}, {elapsed:.5f}, {self.alltime:.5f}")
            return result
    @timer
    def listcomp(N):
        return [x * 2 for x in range(N)]

    @timer
    def mapcall(N):
        return list(map((lambda x: x*2), range(N)))

    result = listcomp(5)
    listcomp(500000)
    listcomp(500000)
    listcomp(1000000)
    print(result)
    print(f"Total time for listcomp {listcomp.alltime}")

    result = mapcall(5)
    mapcall(500000)
    mapcall(500000)
    mapcall(1000000)
    print(result)
    print(f"Total time for mapcall {mapcall.alltime}")

    print(f"Ratio of mapcall/listcomp time {round(mapcall.alltime/listcomp.alltime,3)}")

if True:
    import time

    """Practice using decorator functions with arguments"""
    def deco_args(*args, **kwargs):
        print("In the argument decorator")
        def decorator(f):
            print("In the function decorator")
            def wrapper(*args, **kwargs):
                print("In the wrapper")
                return wrapper

    def timer(label="", trace=False):
        print("In the argument decorator")
        print(f"label: {label}")
        print(f"trace: {trace}")
        def decorator(f):
            print("In the function decorator")
            print(f"f: {f}")
            alltime = 0
            def wrapper(*args, **kwargs):
                print(f"In the wrapper of {f}")
                print(f"args: {args}")
                print(f"kwargs: {kwargs}")
                nonlocal alltime
                start = time.process_time()
                result = f(*args, **kwargs)
                elapsed = time.process_time() - start
                alltime = elapsed + alltime
                if trace:
                    print(f"{label}{f.__name__}, {elapsed:.5f}, {alltime:.5f}")
                return result
            return wrapper
        return decorator

    @timer('==>', True)
    def listcomp(N):
        return [x * 2 for x in range(N)]

    @timer('-->', False)
    def mapcall(N):
        return list(map((lambda x: x*2), range(N)))

    result = listcomp(5)
    listcomp(500000)
    listcomp(500000)
    # listcomp(1000000)
    # print(result)
    # # print(f"Total time for listcomp {listcomp.alltime}")
    #
    result = mapcall(5)
    mapcall(500000)
    mapcall(500000)
    # mapcall(1000000)
    # print(result)
    # # print(f"Total time for mapcall {mapcall.alltime}")

    # print(f"Ratio of mapcall/listcomp time {round(mapcall.alltime/listcomp.alltime,3)}")












