
def my_decorator(func):
    # def wrapper():
    #     func()
    # return wrapper()
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper

@my_decorator
def hello(name):
    print(f"Hello {name}")

#hello = my_decorator(hello)