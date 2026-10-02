#create a generator function called multiples_of_3 that generators the first 5 multiples of 3 using yield.Use for loop to print the values.
def multiples_of_3():
    for i in range(1,6):
        yield i*3
for num in multiples_of_3():
    print(num)