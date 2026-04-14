# Create a decorator to print the function name and the values of its arguments every time the function is called.

def name(func):
    def wrapper(*args, **kwargs):
        