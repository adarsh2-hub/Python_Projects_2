#create the generator function called characters() that takes a string and uses yield to produce one character at a time.
def characters(text):
    for char in text:
        yield char
for ch in characters("python"):
    print(ch)