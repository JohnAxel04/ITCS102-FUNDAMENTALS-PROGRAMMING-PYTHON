#while loop

me = True

while me == True:
    moon = input("(Yes or No): ")

    if moon.lower() == "yes":
        print("COntinue")
        continue
    elif moon.lower() == "no":
        print("Stop")
        break
    else:
        print("Error input")
        continue