#Write a python program using a with statement to open practice.txt in read mode and print its contents. The file contains: I am learning Python.
with open("practice.txt","w") as file:
    file.write("I am learning Python..")
with open("practice.txt","r") as file:
    content=file.read()
    print(content)