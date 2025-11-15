print("Adding anime to Dictionary")

li = {} #empty dictionary

tr = True 

def search(ky): #Function of search
    print("Searching....")
    print(f"Result shows {li[ky]}")

def print_anime(): #Fuction of Print
    for k,t in li.items():
        print(f"Keys {k} Title {t}")

while tr == True:
    new = input("Key to call the anime: ")
    news = input("Title of the anime: ")

    li[new] = news #To Add The Putted input

    choice = input("Would you like to continue\ny - yes\nn - No\nP - Print\nS - Search\nTyping..... ").lower()

    if choice == "y": 
        print("Continuing...")
        continue
    elif choice == "n": #Stopper
        print("exiting....")
        print("Program Stop")
        break
    elif choice == "p": #print
        print("=========================")
        print("Printing....")
        print_anime()
        print("=========================")
        continue
    elif choice == "s": #Search
        srch = input(f"Put the key: ")
        print("exiting....")
        search(srch)
        continue
    else:
        print("Error! Invalid Choice")
        