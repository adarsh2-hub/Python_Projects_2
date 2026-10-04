#Write a python program using with to create a file named numbers.txt and write the numbers 1 to 5, each on a new line.
with open("numbers.txt","w") as file:
    for i in range(1,6):
        file.write(str(i)+"\n")
with open("numbers.txt","r") as file:
    content=file.read()
    print(content)