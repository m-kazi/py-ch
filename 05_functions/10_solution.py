# Factorial of 5 = 5*4*3*2*1
# to find out factorial of 5 we will calculate 4 first and so on...


# for recursive function always need an exit point
def factorial(n):
    # exit point
    if n == 0:
        return 1
    else:
        # calling function inside the function
        return n * factorial(n - 1)


print(factorial(3))
