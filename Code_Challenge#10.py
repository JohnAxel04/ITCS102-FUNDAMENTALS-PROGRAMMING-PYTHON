#Make a pyramid using for loop

print("\t\t *")
for me in range(2,11):
    for u in range(10,me,-1):
        print(" ",end=" ")
    for tm in range(1,me,1):
        print("*",end=" ")
    for hm in range(1,me,1):
        print("*",end=" ")
    print()
