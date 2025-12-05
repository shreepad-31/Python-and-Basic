# Write a decorator that measures the time a function takes to execute.

import time

def timer(func):
    def wrapper(*args, **kwargs):
        strt = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - strt} time.")
        return result
    return wrapper

@timer
def ex_func(n):
    time.sleep(n)

ex_func(n = int(input("Enter a number: ")))