def basic(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@basic
def hello():
    print("Hello World")

hello()