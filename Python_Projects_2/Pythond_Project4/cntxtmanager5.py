#Create a file named welcome.txt using a with statement.Write these message into the file: Welcome to Python! I am learning Context Managers. Then use another with statement to read the file and print the message.
with open("welcome.txt","w") as file:
    file.write("Welcome to Python!\nI am learning Context Managers.")
with open("welcome.txt","r") as file:
    content=file.read()
    print(content)