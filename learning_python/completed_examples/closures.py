def f(x):
    x = 0
    def g(y):
        nonlocal x
        return x + y

    return g  # Return a closure.


def h(x):
    return lambda y: x + y  # Return a closure.


# Assigning specific closures to variables.
a = f(10)
b = h(2)

# Using the closures stored in variables.
print(f"{a(5)}")
print(f"{b(5)}")

# Using closures without binding them to variables first.
print(f"{f(100)(5)}")  # f(1) is the closure.
print(f"{h(100)(10)}")  # h(1) is the closure.