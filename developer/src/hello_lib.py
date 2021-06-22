def my_decorator(func):
    def wrapper():
        func()
    return wrapper()

def hello(name):
    print(f"Hello {name}")

hello = my_decorator(hello)