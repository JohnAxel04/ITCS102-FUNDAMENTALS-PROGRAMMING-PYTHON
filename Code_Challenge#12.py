#Triangle using for loop with set of numbers

for i in range(1,7):
    for l in range(7,i,-1):#For spaces
        print(" ",end=" ")
    for m in range(i,0,-1):#left triangle/reverse number
        print(m,end=" ")
    for p in range(2,i + 1):#right triangle
        print(p,end=" ")
    print()#to print from top to bottom