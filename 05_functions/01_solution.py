# 1. Basic Function Syntax
# Problem: Write a function to calculate and return the square of a number.

def square(number):
    return number**2

num = int(input("Enter a number: "))
result = square(num)
print(result)
print(square(5))