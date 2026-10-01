def start_decorator(func):
    def wrapper():
        print("Starting..")
        func()
    return wrapper
@start_decorator
def work():
    print("Work is running..")
work()