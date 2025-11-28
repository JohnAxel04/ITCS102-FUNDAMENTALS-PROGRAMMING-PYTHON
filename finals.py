import os
import time
# from dictionary import *
# from floop import *
# from ifelif import *
# from list import *
# from math import *
# from print import *
# from wloop import *


print(" -------------------------------") 
print("|\t Hello Welcome To\t|")
print("|\t  My FIle System\t|")             #Not belong to the while loop so that, if the user want to go back to menu the welcome something wont show again and will directed to the menu options
print(" -------------------------------")
main = input("Want to proceed(y/n): ").lower()
os.system('cls')

while True:
    
    if main == "y":
        print("Loading Menu Options....")
        
        time.sleep(3)
        os.system('cls')
        print(" -------------------------------")
        print("|\t      MENU\t\t|")
        print(" -------------------------------")
        print(" -------------------------------")
        print("| \to\t\to\t|")
        print("| \t\t\t\t|")
        print("|  P - Print Activity\t\t|")
        print("|  A - Arithmetic Activity\t|")
        print("|  I - If/Else Statement\t|")
        print("|  F - For loop Activity\t|")
        print("|  W - While loop Activity\t|")
        print("|  L - List Activity\t\t|")
        print("|  C - Code Challenge\t\t|")
        print("| \t\t\t\t|")
        print("|  E - Exit\t\t\t|")
        print(" -------------------------------")
        print("Choose ")
        menu = input("Typing... ").lower()
        os.system('cls')
        if menu == "p":
            print(f"user input --> {menu} = PRINT ACTIVITY")
            print("Loading....")
            time.sleep(3)
            print(" -------------------------------")
            print("| \to\t\to\t|")
            print("| \t\t\t\t|")
            print("|  \t1 - Activity1\t\t|")
            print("|  \t2 - Activity2\t\t|")
            print("|  \t3 - Activity3\t\t|")
            print("|  \t4 - Activity4\t\t|")
            print("| \t\t\t\t|")
            print("| \tE - Exit\t\t|")
            print(" -------------------------------")
            print("Choose ")
            menus = input("Typing... ").lower()
            os.system('cls')
            if menus == "e".lower():
                print("Exiting.....")
                print("(E - Exit or C - Continue to Menu)")
                ex = input("Typing... ").lower()
                if ex == "c":
                    continue
                elif ex == "e":
                    print("Thank You For Using my Ai")
                    print("Bye bye")
                    break
                else:
                    print("Error Input.... ")

            elif menus == "1":
                print("You have selected Activity1")
                print("Loading Activity....")
                time.sleep(3)
                # activity1()

            elif menus == "2":
                print("You have selected Activity2")
                print("Loading Activity....")
                time.sleep(3)
                # activity2()

            elif menus == "3":
                print("You have selected Activity3")
                print("Loading Activity....")
                time.sleep(3)
                # activity3()

            elif menus == "4":
                print("You have selected Activity4")
                print("Loading Activity....")
                time.sleep(3)
                # activity4()
            else:
                print("Unfortunate Not in the Options")  
                print("Try Again")
                time.sleep(3)
                continue

        elif menu == "a":
            print(f"user input --> {menu} = PRINT ACTIVITY")
            print("Loading....")
            time.sleep(3)
            print(" -------------------------------")
            print("| \to\t\to\t|")
            print("| \t\t\t\t|")
            print("|  \t5 - Activity5\t\t|")
            print("|  \t6 - Activity6\t\t|")
            print("|  \t7 - Activity7\t\t|")
            print("|  \t8 - Activity8\t\t|")
            print("| \t\t\t\t|")
            print("| \tE - Exit\t\t|")
            print(" -------------------------------")
            print("Choose ")
            menus = input("Typing... ").lower() 
            os.system('cls')
            if menus == "e".lower():
                print("Exiting.....")
                print("(E - Exit or C - Continue to Menu)")
                ex = input("Typing... ").lower()
                if ex == "c":
                    continue
                elif ex == "e":
                    print("Thank You For Using my Ai")
                    print("Bye bye")
                    break
                else:
                    print("Error Input.... ") 
            elif menus == "5":
                print("You have selected Activity1")
                print("Loading Activity....")
                time.sleep(3)
                # activity1()

            elif menus == "6":
                print("You have selected Activity2")
                print("Loading Activity....")
                time.sleep(3)
                # activity2()

            elif menus == "7":
                print("You have selected Activity3")
                print("Loading Activity....")
                time.sleep(3)
                # activity3()

            elif menus == "8":
                print("You have selected Activity4")
                print("Loading Activity....")
                time.sleep(3)
                # activity4()
            else:
                print("Unfortunate Not in the Options")  
                print("Try Again")
                time.sleep(3)
                continue  
        elif menu == "i":
            print(f"user input --> {menu} = PRINT ACTIVITY")
            print("Loading....")
            time.sleep(3)
            print(" -------------------------------")
            print("| \to\t\to\t|")
            print("| \t\t\t\t|")
            print("|  \t1 - Activity5\t\t|")
            print("|  \t2 - Activity6\t\t|")
            print("|  \t3 - Activity7\t\t|")
            print("|  \t4 - Activity8\t\t|")
            print("| \t\t\t\t|")
            print("| \tE - Exit\t\t|")
            print(" -------------------------------") 
            print("Choose ")
            menus = input("Typing... ").lower() 
            os.system('cls')
            if menus == "e".lower():
                print("Exiting.....")
                print("(E - Exit or C - Continue to Menu)")
                ex = input("Typing... ").lower()
                if ex == "c":
                    continue
                elif ex == "e":
                    print("Thank You For Using my Ai")
                    print("Bye bye")
                    break
                else:
                    print("Error Input.... ")
            elif menus == "1":
                print("You have selected Activity1")
                print("Loading Activity....")
                time.sleep(3)
                # activity1()

            elif menus == "2":
                print("You have selected Activity2")
                print("Loading Activity....")
                time.sleep(3)
                # activity2()

            elif menus == "3":
                print("You have selected Activity3")
                print("Loading Activity....")
                time.sleep(3)
                # activity3()

            elif menus == "4":
                print("You have selected Activity4")
                print("Loading Activity....")
                time.sleep(3)
                # activity4()
            else:
                print("Unfortunate Not in the Options")  
                print("Try Again")
                time.sleep(3)
                continue
        elif menu == "f":
            print(f"user input --> {menu} = PRINT ACTIVITY")
            print("Loading....")
            time.sleep(3)
            print(" -------------------------------")
            print("| \to\t\to\t|")
            print("| \t\t\t\t|")
            print("|  \t1 - Activity5\t\t|")
            print("|  \t2 - Activity6\t\t|")
            print("|  \t3 - Activity7\t\t|")
            print("|  \t4 - Activity8\t\t|")
            print("| \t\t\t\t|")
            print("| \tE - Exit\t\t|")
            print(" -------------------------------")
            print("Choose ")
            menus = input("Typing... ").lower()  
            os.system('cls')
            if menus == "e".lower():
                print("Exiting.....")
                print("(E - Exit or C - Continue to Menu)")
                ex = input("Typing... ").lower()
                if ex == "c":
                    continue
                elif ex == "e":
                    print("Thank You For Using my Ai")
                    print("Bye bye")
                    break
                else:
                    print("Error Input.... ")
            elif menus == "1":
                print("You have selected Activity1")
                print("Loading Activity....")
                time.sleep(3)
                # activity1()

            elif menus == "2":
                print("You have selected Activity2")
                print("Loading Activity....")
                time.sleep(3)
                # activity2()

            elif menus == "3":
                print("You have selected Activity3")
                print("Loading Activity....")
                time.sleep(3)
                # activity3()

            elif menus == "4":
                print("You have selected Activity4")
                print("Loading Activity....")
                time.sleep(3)
                # activity4()
            else:
                print("Unfortunate Not in the Options")  
                print("Try Again")
                time.sleep(3)
                continue
        elif menu == "w":
            print(f"user input --> {menu} = PRINT ACTIVITY")
            print("Loading....")
            time.sleep(3)
            print(" -------------------------------")
            print("| \to\t\to\t|")
            print("| \t\t\t\t|")
            print("|  \t1 - Activity5\t\t|")
            print("|  \t2 - Activity6\t\t|")
            print("|  \t3 - Activity7\t\t|")
            print("|  \t4 - Activity8\t\t|")
            print("| \t\t\t\t|")
            print("| \tE - Exit\t\t|")
            print(" -------------------------------")
            print("Choose ")
            menus = input("Typing... ").lower()
            os.system('cls')
            if menus == "e".lower():
                print("Exiting.....")
                print("(E - Exit or C - Continue to Menu)")
                ex = input("Typing... ").lower()
                if ex == "c":
                    continue
                elif ex == "e":
                    print("Thank You For Using my Ai")
                    print("Bye bye")
                    break
                else:
                    print("Error Input.... ")
            elif menus == "1":
                print("You have selected Activity1")
                print("Loading Activity....")
                time.sleep(3)
                # activity1()

            elif menus == "2":
                print("You have selected Activity2")
                print("Loading Activity....")
                time.sleep(3)
                # activity2()

            elif menus == "3":
                print("You have selected Activity3")
                print("Loading Activity....")
                time.sleep(3)
                # activity3()

            elif menus == "4":
                print("You have selected Activity4")
                print("Loading Activity....")
                time.sleep(3)
                # activity4()
            else:
                print("Unfortunate Not in the Options")  
                print("Try Again")
                time.sleep(3)
                continue
        elif menu == "l":
            print(f"user input --> {menu} = PRINT ACTIVITY")
            print("Loading....")
            time.sleep(3)
            print(" -------------------------------")
            print("| \to\t\to\t|")
            print("| \t\t\t\t|")
            print("|  \t1 - Activity5\t\t|")
            print("|  \t2 - Activity6\t\t|")
            print("|  \t3 - Activity7\t\t|")
            print("|  \t4 - Activity8\t\t|")
            print("| \t\t\t\t|")
            print("| \tE - Exit\t\t|")
            print(" -------------------------------")
            print("Choose ")
            menus = input("Typing... ").lower()
            os.system('cls')
            if menus == "e".lower():
                print("Exiting.....")
                print("(E - Exit or C - Continue to Menu)")
                ex = input("Typing... ").lower()
                if ex == "c":
                    continue
                elif ex == "e":
                    print("Thank You For Using my Ai")
                    print("Bye bye")
                    break
                else:
                    print("Error Input.... ")
            elif menus == "1":
                print("You have selected Activity1")
                print("Loading Activity....")
                time.sleep(3)
                # activity1()

            elif menus == "2":
                print("You have selected Activity2")
                print("Loading Activity....")
                time.sleep(3)
                # activity2()

            elif menus == "3":
                print("You have selected Activity3")
                print("Loading Activity....")
                time.sleep(3)
                # activity3()

            elif menus == "4":
                print("You have selected Activity4")
                print("Loading Activity....")
                time.sleep(3)
                # activity4()
            else:
                print("Unfortunate Not in the Options")  
                print("Try Again")
                time.sleep(3)
                continue
        elif menu == "c":
            print(f"user input --> {menu} = PRINT ACTIVITY")
            print("Loading....")
            time.sleep(3)
            print(" -------------------------------")
            print("| \to\t\to\t|")
            print("| \t\t\t\t|")
            print("|  \t1 - Activity5\t\t|")
            print("|  \t2 - Activity6\t\t|")
            print("|  \t3 - Activity7\t\t|")
            print("|  \t4 - Activity8\t\t|")
            print("| \t\t\t\t|")
            print("| \tE - Exit\t\t|")
            print(" -------------------------------")
            print("Choose ")
            menus = input("Typing... ").lower()
            os.system('cls')
            if menus == "e".lower():
                print("Exiting.....")
                print("(E - Exit or C - Continue to Menu)")
                ex = input("Typing... ").lower()
                if ex == "c":
                    continue
                elif ex == "e":
                    print("Thank You For Using my Ai")
                    print("Bye bye")
                    break
                else:
                    print("Error Input.... ")
            elif menus == "1":
                print("You have selected Activity1")
                print("Loading Activity....")
                time.sleep(3)
                # activity1()

            elif menus == "2":
                print("You have selected Activity2")
                print("Loading Activity....")
                time.sleep(3)
                # activity2()

            elif menus == "3":
                print("You have selected Activity3")
                print("Loading Activity....")
                time.sleep(3)
                # activity3()

            elif menus == "4":
                print("You have selected Activity4")
                print("Loading Activity....")
                time.sleep(3)
                # activity4()
            else:
                print("Unfortunate Not in the Options")  
                print("Try Again")
                time.sleep(3)
                continue
        elif menu == "e":
            print("Thank You For Using my System")
            print("Bye bye")
            break   
        else:
            print("Unfortunate Not in the Options")  
            print("Try Again")
            continue
    elif main == "n":
        print("Thank you very much")
        break