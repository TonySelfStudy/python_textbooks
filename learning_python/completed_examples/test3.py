
def f1(a, *b, c=6, **d):
    print(a, b, c, d)

def f2(a, b, c=6, **d):
    print(a, b, c, d)

def func(a, b, c):
    a = 2
    b[0] = 'x'
    c['a'] = 'y'

# timer(min, 2, 1_000)
# timer(str.upper, 'spam')

# f1(1, [2, 3], 8, **dict(x=4, y=5))
# f1(1, *(2, 3), 8, **dict(x=4, y=5))
# f1(1, *[2, 3], 8, **dict(x=4, y=5))
# f2(1, (2, 3), 8, dict(x=4, y=5))

# l = 1
# m = [1]
# n = {'a': 0}
# func(l, m, n)
# print(l, m, n)


V = [1, 2, 3]
print(V)
M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(M)

V1 = [x**2 for x in V]
print(V1)
V2 = [[x**2 for x in V]]
print(V2)

M1 = [col for row in M for col in row]
print(M1)

M2 = [[col for col in row] for row in M]
print(M2)


# M2 = []
# for row in M:
#     M2.append(row)
# print(M2)
#
# M3 = []
# for row in M:
#     for col in row:
#         M3.append(col)
# print(M3)