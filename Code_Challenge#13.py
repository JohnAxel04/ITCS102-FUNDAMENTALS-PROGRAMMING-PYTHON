#All odd will calculated and skip if even


name = input("Whats your name: ")

odd = 0
numb = "" #More like a list
ys = True

while ys == True:
    num = eval(input("Put a number: "))
    if num % 2 == 1:
        print("Odd Detected")
        odd += num
        numb += str(num) + "," #Will add coma each number
        continue
    elif num == 0: #Will stop if user input 0
        print("Bye Bye")
        break
    else:
        print("Even detected")
        print("Skipping")
        continue
print(f"Total of all odd number: {odd}")
print(f"All odd number: {numb}")
