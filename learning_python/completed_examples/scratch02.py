from inspectors import Inspector
import sys
import builtins
#import ex

class PropTest:
    def __init__(self):
        self._age = 30

    def getage(self):
        return self._age

    def setage(self,value):
        print(f'In setage, setting age to {value}')
        self._age = value
    age = property(getage, setage, None, None)


class MethodTest:

    def instance_method(self, arg):
        print(f'In instance_method.\targ= {arg}\n')

    def class_method(cls, arg):
        print(f'In class_method.\targ= {arg}')
        print(f'cls.__name__ = {cls.__name__}')
        attrs = dir(cls)
        for attr in attrs:
            print(f'{attr} = {getattr(cls, attr)}')
        print()

    def static_method(arg):
        print(f'In static_method.\targ= {arg}')
        print(dir())
        print()

    static_method = staticmethod(static_method)
    class_method = classmethod(class_method)


if False:
    x = PropTest()
    print(x.age)
    x.age = 42
    print(x.age)
    print(dir(x))
    print(dir(PropTest))

if False:
    mt = MethodTest()
    mt.instance_method('passed literal1')
    MethodTest.static_method('passed literal2')
    mt.class_method('passed literal3')
    MethodTest.class_method('passed literal4')

if False:
    insp = Inspector()

    try:
        try:
            1/0
        except Exception as e:
            insp.climb_dir(e, None)
            # raise TypeError
            raise TypeError from e
            #badname
    except Exception as f:
        insp.climb_dir(f, None)
        open('nosuchfile')

if False:
    class General(Exception): pass
    class Specific1(General): pass
    class Specific2(General): pass
    insp = Inspector()
    # insp.climb_dir(sys, None)


    def raiser0():
        x = General()
        raise x

    def raiser1():
        x = Specific1()
        raise x

    def raiser2():
        x = Specific2()
        raise x

    for call in (raiser0, raiser1, raiser2):
        for i in dir(builtins):
            print(i)
        exit()

        x = dir()
        y = __builtins__
        print(y)
        for i in dir(y):
            print(i)
        print(x)
        try:
            call()
        except General as g:
            i = sys.exc_info()[0]
            print(i)

            # print("caught: %s" % )
            # print(g.__class__)
            # print(g.__class__.__name__)

if True:
    pass
