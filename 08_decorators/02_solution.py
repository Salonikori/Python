# Problem 2: Debugging Function Calls
# Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.

def printer(func):
    def wrapper(*args, **kwargs):
        arg_values = ", ".join(str(arg) for arg in args)
        kwarg_values = ", ".join(f"{k}={v}" for k,v in kwargs.items())
        result = func(*args, **kwargs)
        print(f"The function is {func.__name__} , arg is {arg_values} and kwargs is {kwarg_values}")
        return result
    return wrapper

@printer
def greet(name, greet = "Hello"):
    return f"{greet}, {name}"

greet("Mehta", greet = "Namaste")
greet("Jethala", "Jai Shree Krishna")