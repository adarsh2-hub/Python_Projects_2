#Create a file named student.txt using a with statement. Write these two lines the file: Name:Adarsh and Course:BCA. Requirements:Use with open() and "w" mode.
with open("student.txt","w") as file:
    file.write("Name: Adarsh")
    file.write("   Course: BCA")
with open("student.txt","r") as file:
    content=file.read()
    print(content)