# 3. Polymorphism in Functions
# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

def multiply(a, b):
    return a*b

print(multiply(3,8))
print(multiply("abc", 5))
print(multiply(5, "abc"))