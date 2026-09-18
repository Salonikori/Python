# 8. Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def display(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

display(name = "Jethalal", power = "Money")
display(name = "Iyer")
display(name = "Taarak Mehta", power = "Books", friend = "Jethalal")