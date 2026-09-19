# Problem 1: Timing Function Execution
# Problem: Write a decorator that measures the time a function takes to execute.

import time
def timer(fun):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fun(*args, **kwargs)
        end = time.time()
        print(f"The function {fun.__name__} take {end-start} time")
        return result
    return wrapper

@timer
def trial_function(t):
    time.sleep(t)

trial_function(3)