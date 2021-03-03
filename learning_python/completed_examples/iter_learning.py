# Learning Iterables a little better
#
from builtins import range

if False:
    L = [1, 2, 3]
    I = iter(L)
    print(I)

    x = I.__next__()
    print(I)
    print(x)

    x = I.__next__()
    print(I)
    print(x)

    x = I.__next__()
    print(I)
    print(x)

    x = I.__next__()
    print(I)
    print(x)

if False:
    f = open('sample_text.txt')
    print(f)
    a = iter(f)
    print(a == f)
    print(a is f)

    x = f.__next__()
    print(x, end='')

    x = f.__next__()
    print(x, end='')

    x = f.__next__()
    print(x, end='')

    x = f.__next__()
    print(x, end='')

    x = f.__next__()
    print(x, end='')

if False:
    r = range(10)
    print(f'len(r)={len(r)}')

    i = iter(r)
    print(dir(i))

    i.__next__()
    i.__next__()
    y = i.__next__()
    print(y)

    print(r[-2])
    r[-1] = 100

    for x in r:
        print(x)

    print(y)
    print(x)

if False:
    r = range(10)
    print(f'len(r)={len(r)}')

    i1 = iter(r)
    i2 = iter(r)

    print(i1.__next__())
    print(i1.__next__())
    print(i1.__next__())
    print(i1.__next__())

    print(i2.__next__())
    print(i2.__next__())

    print(i1.__next__())
    print(i1.__next__())

if False:
    m = map(float, (-1, 0, 1,))
    i1 = iter(m)
    i2 = iter(m)
    print(m==i1, m==i2, i1==i2)

    print(m)
    print(next(m))
    print(m.__next__())
    print(next(m))

    for x in m:
        print(x)

if False:
    l = [10, 40, 30, 20]
    d = {3: 'c', 1: 'a', 2: 'b', 4: 'd'}
    # print(l)
    # print(sorted(l))
    # print(l)
    # print(l.sort())
    # print(l)

    print(d)
    print(sorted(d.keys()))
    print(d)

    print(d)

if True:
    pass
