import math


def circle_stats(radius):
    area = round((math.pi * radius**2), 2)
    circumference = round((2 * math.pi * radius), 2)
    return area, circumference


# holding 2 values returning from the function
a, c = circle_stats(3)


print(f"Area: {a} Circumference: {c}")
