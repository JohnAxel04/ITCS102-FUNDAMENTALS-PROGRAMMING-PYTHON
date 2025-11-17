import os
os.system('cls')
diction = {}

while True:
    print("Select From options Below\nA - Add Information\nB - Search Information\nC - Delete Information\nD - To Modify Information\nE - Exit")

    new = input("Typing...       ").lower()

    if new == "a":
        print("Adding Information")
        ky = input("Key to call for the Information: ")
        fname = input("Input Student First Name: ")
        lname = input("Input Student Last Name: ")
        email = input("Input Student Email: ")

        dc = {ky : [fname,lname,email]}
        print("Data saved")
        os.system('cls')
        continue
    elif new == "b":
        os.system('cls')
        srch = input("key of the information: ")

        for q in dc.keys():
            if  srch in dc.keys():
                print("record Found")

                print("Record Info")
                print("--------------------------")
                for i in dc[srch]:
                    print(i)
                print("--------------------------")
            else:
                print("Information not Found")  
        continue
    elif new == "c":
        pass
    elif new == "d":
        pass
    elif new == "e":
        print("Exiting")
        break
    else:
        print("Invalid Input")
    

