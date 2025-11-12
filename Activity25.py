from Activity25_1 import *

name  = input("Whats is your name: ")

print(f"Welcome {name} to my File compiler")

t = True

while t == True:
    print("Select a program")
    print("A - Activity1\nB - Activity2\nC - Activity3\nD - Activigty 4\nE - Exit")

    new = input("What program would you like to run: ").lower()

    if new == "a":
        activity1()
        continue
    elif new == "b":
        activity2()
        continue
    elif new == "c":
        activity3()
        continue
    elif new == "d":
        activity4()
    elif new == "e":
        print("Thank you for sunshine")
        break
    else:
        print("error input")

