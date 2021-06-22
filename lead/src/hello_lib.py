def my_decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper

@my_decorator
def hello(name):
    print(f"Hello {name}")