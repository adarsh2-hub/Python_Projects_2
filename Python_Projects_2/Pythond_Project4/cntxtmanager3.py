#Create a file named marks.txt using a with statement and write these marks: Python:85 , Java:78 , HTML:90. Then read the file using another with statement and print all the contents.
with open("marks.txt","w") as file:
    file.write("Python:85  Java:78  HTML:90")
with open("marks.txt","r") as file:
    content=file.read()
    print(content)