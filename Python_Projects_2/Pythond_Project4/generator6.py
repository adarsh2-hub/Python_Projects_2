#create the generator function called odd_numbers() that generators the first 5 odd numbers using yield.
def odd_numbers():
    for num in range(1,10,2):
        yield num
for odd in odd_numbers():
    print(odd)