name = input("Whats your name: ")
num = eval(input("Put a number: "))

odd = 0
even = 0

while num != 0:
    num = eval(input("Put a number: "))
    if num % 2 == 0:
        even += num
    elif num % 2 == 1:
        odd += num
    else:
        print("error input")
print(f"Total of all even number: {even}")
print(f"Total of all odd number: {odd + 1}")
print(f"{odd}")