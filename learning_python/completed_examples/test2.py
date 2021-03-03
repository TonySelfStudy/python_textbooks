from test1 import myfun

if False:
    a=4
    b=5
    print(f"a={a}")
    print(f"test1.a={test1.a}")

    "Stringme"

    dir_test1 = dir(test1)
    dir_blank = dir()

    for val in dir_test1:
        print(val)

    print("***")

    for val in dir_blank:
        print(val)

if False:
    list1 = [1, 2, 3]
    list2 = list1 + [4] + list1
    print(list2)

    str1 = 'this is a string'
    print(f"len=*{len(str1)}*")
    print(f"min=*{min(str1)}*")
    print(f"max=*{max(str1)}*")

if False:
    list3 = [2, 3, 4]
    list4 = list3 * 2
    print(list4)
    list4[0] = -99
    print(list4)


if False:
    a = ["John", "Charles", "Mike"]
    b = ["Jenny", "Christy", "Monica"]
    c = ["tom", "joe", "sam"]

    x = zip(a, b, c)
    for i in x:
        print(i)

    y = dict(x)
    print(y)

myfun()


