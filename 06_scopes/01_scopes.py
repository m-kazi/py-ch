username = "kazzcode"


def func():
    username = "kazi"
    print(username)


# print(username)
# func()

# another example

x = 99


def func2(y):
    z = x + y
    return z


result = func2(1)
print(result)


# closure example


def f1():
    x = 88

    def f2():
        print(x)

    return f2


my_result = f1()
my_result()


# another closure example


def coffee_coder(num):
    def actual(x):
        return x**num

    return actual


# here 'f' is holding 'actual' definition only with 'num = 2'
f = coffee_coder(2)
g = coffee_coder(3)

print(f(2))
print(g(3))
