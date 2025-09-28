tot = 0
for x in range(1, 11,1): 
    name = eval(input("Put Number: "))
    if name % 2:
        tot += name
print("The Sum of all odd number is",tot) 
