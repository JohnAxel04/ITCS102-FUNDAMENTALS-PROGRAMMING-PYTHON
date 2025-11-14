print("Adding anime to Dictionary")

li = {}

tr = True

def search(ky):
    print("Searching....")
    print(f"Result shows {li[ky]}")

def print_anime():
    for k,t in li.items():
        print(f"Keys {k} Title {t}")

while tr == True:
    new = input("Key to call the anime: ")
    news = input("Title of the anime: ")

    li[new] = news

    choice = input("Would you like to continue\ny - yes\nn - No\nP - Print\nS - Search\nTyping..... ").lower()

    if choice == "y":
        print("Continuing...")
        continue
    elif choice == "n":
        print("exiting....")
        print("Program Stop")
        break
    elif choice == "p":
        print("=========================")
        print("Printing....")
        print_anime()
        print("=========================")
        continue
    elif choice == "s":
        srch = input(f"Put the key: ")
        print("exiting....")
        search(srch)
        continue
    else:
        print("Error! Invalid Choice")
        