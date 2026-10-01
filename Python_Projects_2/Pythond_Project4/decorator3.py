def timer_decorator(func):
    def wrapper():
        print("Starting timer..")
        func()
    return wrapper
@timer_decorator
def calculator():
    print("Calculating..")
calculator()