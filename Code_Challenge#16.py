
import os
import json
os.system('cls') #To clear the menu when putted something
diction = {} #empty dictionary

while True: 
    print("Select From options Below\nA - Add Information\nB - Print all\nc - Search Information\nd - Delete Information\ne - To Edit File\nF - Export Data\nG - Import Data\nP - Exit") #Menu List

    new = input("Typing...       ").lower() #lower so the putted letter can be lower case or upper case

    if new == "a":
        print("Adding Information")
        ky = input("Key to call for the Information: ")
        fname = input("Input Student First Name: ")
        lname = input("Input Student Last Name: ")
        course = input("Input Course: ")
        email = input("Input Student Email: ")

        diction[ky] = [fname,lname,course,email] #It will add multiple data to the dictionary 
        print("Data saved")
        os.system('cls')
        continue
    elif new == "c":
        os.system('cls')
        srch = input("key of the information: ")

        for a in diction.keys():# for q in diction(): #Search, For loop will help us connect to the dictionary
            if  srch in diction.keys(): #it will check if  the Input keys is in the dictionary
                print("record Found")
            
                print("Record Info")
                print("--------------------------")
                for y in diction[srch]:
                     print(f": {y}")
                print("--------------------------")
            else:
                print("Information not Found")  
            break
        continue
    elif new == "b":
        os.system('cls')
        for a,p in diction.items(): #for loop it will manage all the information in the dictioanary
            print(f"STUDENTS ID {a}: STUDENT RECORD {p}") #it will now print all the items in dictionary
        continue
    elif new == "d":
        os.system('cls')
        print("Delete existing record")
        srch = input("key of the information: ")
        if  srch in diction.keys(): #it will check if  the Input keys is in the dictionary
            

            print("Record deleted")
            print("--------------------------")
            for i in diction[srch]:
                    print(f": {i}")

            diction.pop(srch)
            print("Record deleted")
        else:
            print("Information cannot found") 
        continue
    elif new == "e":
        os.system('cls')
        print("Record Modification")
        
        srch = input("key of the information: ")

        for a in diction[srch]:
                    print(f": {a}")

        
        fname = input("Input Student First Name: ")
        lname = input("Input Student Last Name: ")
        course = input("Input Course: ")
        email = input("Input Student Email: ")

        diction[srch][0] = fname
        diction[srch][1] = lname
        diction[srch][2] = course
        diction[srch][3] = email

        print("Data Updated")

        continue
    elif new == "f":
        os.system('cls')
        with open("diction.json","w") as new_file:
            json.dump(diction,new_file, indent=4)
            print("Data Exported")
        continue
    elif new == "g":
        os.system('cls')
        with open("diction.json","r") as new_file:
            diction_json = json.load(new_file)

        diction = diction_json
        print("Data Imported")

        continue
    elif new == "p":
        print("Exiting")
        break
    else:
        print("Invalid Input")
    



