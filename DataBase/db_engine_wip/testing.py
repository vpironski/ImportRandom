import os
from open_module import Open_Database
from create_module import Create_Database


# Getting user input
flag = True
while flag:
    user = input(" What would you like to do (Create/Open/Quit): ")
    user.lower


    # Checking user Input
    if user == "create":
        file_name = input("Enter the file you want to create: ")
        db = Create_Database(file_name)
        flag = False

    elif user == "open":
        file_name = input("Enter the file you want to open: ")
        db = Open_Database(file_name)
        print(db.colons)
        flag = False

    elif user == "quit":
        flag = False
    
    else:
        print("You have entered an invalid command. Please try again!")