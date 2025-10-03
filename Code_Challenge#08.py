print("Multiplication Table Maker")
name = eval(input("Put a Number: "))
print("Multiplication Table For: ",name)
for u in range(1 ,11):
  total = name * u
  print(name,"x",u,"=", total)
