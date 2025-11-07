import random



num = random.randint(1,10)

tries = 0
we = True

while we == True:
    g = int(input("What number u guess(1-10): "))
    tries += 1

    if g == num:
        print("Congratulation")
        print(f"the number is {num}")
        print(f"YOu online took {tries} tries")
        break

    else:
        print("youre wrong")
        continue
 