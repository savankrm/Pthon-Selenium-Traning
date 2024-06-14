#  write a python program using the keyword ‘nonlocal’.

# First Function
def f():
    x = 10

    # Nested Function
    def g():
        nonlocal x
        x = 1

    g()
    print(x)


f()