#create a generator function called count_numbers() that uses yield to produce: 1,2,3,4,5. Then uses for loop to print all the values.
def count_numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
for numbers in count_numbers():
    print(numbers)