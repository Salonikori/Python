# 10. Recursive Function
# Problem: Create a recursive function to calculate the factorial of a number.

def fact(number):
    if number == 0:
        return 1
    else:
        return number * fact(number-1)


print(fact(5))