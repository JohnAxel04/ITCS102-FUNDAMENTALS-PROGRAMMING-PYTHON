email = "BSIT-1A"
passw = "secret"

x = input("Email: ")
y = input("Password: ")
if x.lower == email and y.lower == passw:
	print("Grant Access")
else:
	print("Access Denied")
	
