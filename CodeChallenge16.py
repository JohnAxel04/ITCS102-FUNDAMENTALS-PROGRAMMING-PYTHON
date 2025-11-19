import os
os.system('cls') #To clear the menu when putted something
diction = {} #empty dictionary

while True: 
    print("Select From options Below\nA - Add Information\nB - Print all\nc - Search Information\nd - Delete Information\ne - To Modify Information\nE - Exit") #Menu List

    new = input("Typing...       ").lower() #lower so the putted letter can be lower case or upper case

    if new == "a":
        print("Adding Information")
        ky = input("Key to call for the Information: ")
        fname = input("Input Student First Name: ")
        lname = input("Input Student Last Name: ")
        email = input("Input Student Email: ")

        diction[ky] = [fname,lname,email] #It will add multiple data to the dictionary 
        print("Data saved")
        os.system('cls')
        continue
    elif new == "c":
        os.system('cls')
        srch = input("key of the information: ")

        for q in diction.keys(): #Search, For loop will help us connect to the dictionary
            if  srch in diction.keys(): #it will check if  the Input keys is in the dictionary
                print("record Found")

                print("Record Info")
                print("--------------------------")
                for i in diction[srch]:
                    print(i)
                print("--------------------------")
            else:
                print("Information not Found")  
        continue
    elif new == "b":
        os.system('cls')
        for a,p in diction.items(): #for loop it will manage all the information in the dictioanary
            print(f"STUDENTS ID {a}: STUDENT RECORD {p}") #it will now print all the items in dictionary
        continue
    elif new == "d":
        os.system('cls')
        print("Delete existing record")
        srch1 = input("key of the information: ")
        if  srch1 in diction.keys(): #it will check if  the Input keys is in the dictionary
            

            print("Record deleted")
            print("--------------------------")
            for i in diction[srch1]:
                    print(f": {i}")

            diction.pop(srch1)
            print("Record deleted")
        else:
            print("Information cannot found") 
        continue
    elif new == "e":
        print("Exiting")
        break
    else:
        print("Invalid Input")
    

