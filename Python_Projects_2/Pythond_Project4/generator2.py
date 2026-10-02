# create a generator function called even_numbers that uses the yield to generate the even numbers from 2 to 10.
def even_numbers():
    for num in range(2,11,2):
        yield num
for even in even_numbers():
    print(even)