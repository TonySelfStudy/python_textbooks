a=1
b=2
c=3
d = 10
e = 11

print(f"d in the test2 scope={d}")


def myfun():
    d = 5
    print(f"d in the myfun scope={d}")
    print(f"e in the myfun scope={e}")
    return d


myfun()
print(f"d in the test2 scope={d}")