#create the generator function called countdown() that generators numbers from 5 to 1 using yield.
def countdown():
    for num in range(5,0,-1):
        yield num
for count in countdown():
    print(count)