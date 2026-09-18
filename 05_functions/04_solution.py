# 4. Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.
import math

def circle(radius):
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    return area, circumference

a , c = circle(5)
print(f"Area is {a:.2f} and circumference is {c:.2f}")