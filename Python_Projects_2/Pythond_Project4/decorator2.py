def login_decorator(func):
    def wrapper():
        print("Checking login..")
        func()
    return wrapper
@login_decorator
def login():
    print("User logged in..")
login()