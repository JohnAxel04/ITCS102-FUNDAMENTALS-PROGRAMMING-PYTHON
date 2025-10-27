#List and its function


nm = ['apple','donut','coconut','mango','grapes']
nm.append('orange')   #add an item to the last of the list
print(nm)
nm.pop()    #remove the last item
print(nm)
nm.insert(0,'Monggo')   #add item in dif position
print(nm)
for i in nm:
    print(f"{i}  in the basket")    #all fruits one by one with 'in the basket' at the last

mi = 'John Axel De Leon'
for u in mi:
    print(u)    #Will print my name from j to n
print("\nReversed\n")
for q in mi[::-1]:  #will print my name in reverse from n to j
    print(q)
