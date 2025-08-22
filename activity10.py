#Grocery
print("---------------------------\n        Welcome \n---------------------------")
name = input("What is your Name? ")
item = input("What item(Fish/Pork): ")
many = eval(input("How many(1-10): "))
fr = eval(input("How much? "))
pwd = input("are you PWD or Senior(Yes/No): ")
equal = many * fr * .05
man = many * fr
more = man - equal

print("---------------------------")
if pwd.lower() == "yes":
	print("Hello", name, "\nItem: ",item, "\nQuantity: ",many,"\nPrice each: ",fr,"\nTotal: ",man ,"\nDiscount:",equal,"\nTotal w/discount: ",more)
else:
	print("Hello", name, "\nItem: ",item, "\nQuantity: ",many,"\nPrice each: ",fr,"\nTotal: ",man ,"\nDiscount:","\nTotal w/discount: ",man)
