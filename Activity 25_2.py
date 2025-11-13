from Activity1 import Activity1
from Activity2 import Activity2
from activity3 import Activity3
from activity4 import Activity4
from activity5 import Activity5
from activity6 import Activity6
from activity7 import Activity7
from activity8 import Activity8
from activity9 import Activity9
from activity10 import Activity10
from activity11 import Activity11
from activity12 import Activity12
from activity13 import Activity13
from activity14 import Activity14
from activity15 import Activity15
from activity16 import Activity16
from activity17 import Activity17
from activity18 import Activity18
from activity19 import Activity19
from activity20 import Activity20
from activity21 import Activity21
from activity22 import Activity22
from activity23 import Activity23
from activity24_1 import Activity241
from activity24 import Activity24
from activity25 import activity25
from activity25_1 import Activity251
from CodeChallenge1 import ccode1
from CodeChallenge2 import ccode2
from CodeChallenge3 import ccode3
from CodeChallenge4 import ccode4
from CodeChallenge5 import ccode5
from CodeChallenge6 import ccode6
from CodeChallenge7 import ccode7
from CodeChallenge8 import ccode8
from CodeChallenge9 import ccode9
from CodeChallenge10 import ccode10
from CodeChallenge11 import ccode11
from CodeChallenge12 import ccode12
from CodeChallenge13 import ccode13
from CodeChallenge14 import ccode14
from CodeChallenge15 import ccode15


print("Welcome to my AI")
name = input("Welcome! What Youre Name: ")
print(f"Hello {name}")
tr = True
while tr == True:
    print("Choose Between")
    print("1 - Activity\n2 - Challenge\nP - Exit")
    n = input("Choose: ")
    if n == "1":
        print("Welcome to my Activities")
        print("1 = Activity(1-5)\n2 = Activity(6-10)\n3 = Activity(11-15)\n4 = Activity(16-20)\n5 = Activity(20-25)\nM - Menu")
        act1 = eval(input("Choose: "))
        if act1 == 1:
            print("Welcome to my Activities(1-5)")
            print("1 = Activity1\n2 = Activity2\n3 = Activity3\n4 = Activity4\n5 = Activity5\nM - Menu")
            ac1 = input("Choose: ").lower()
            if ac1 == "1":
                print(f"Selected Number: {ac1}")
                print(f"Activity {ac1} now using")
                Activity1()
                continue
            elif ac1 == "2":
                print(f"Selected Number: {ac1}")
                print(f"Activity {ac1} now using")
                Activity2()
                continue
            elif ac1 == "3":
                print(f"Selected Number: {ac1}")
                print(f"Activity {ac1} now using")
                Activity3()
                continue
            elif ac1 == "4":
                print(f"Selected Number: {ac1}")
                print(f"Activity {ac1} now using")
                Activity4()
                continue
            elif ac1 == "5":
                print(f"Selected Number: {ac1}")
                print(f"Activity {ac1} now using")
                Activity5()
                continue
            elif ac1 == "m":
                print("Menu..")
            else:
                print("Error Choose again")
                continue
        elif act1 == 2:
            print("Welcome to my Activities(6-10)")
            print("6 = Activity6\n7 = Activity7\n8 = Activity8\n9 = Activity9\n10 = Activity10\nM - Menu")
            ac2 = input("Choose: ").lower()
            if ac2 == "6":
                print(f"Selected Number: {ac2}")
                print(f"Activity {ac2} now using")
                Activity6()
                continue
            elif ac2 == "7":
                print(f"Selected Number: {ac2}")
                print(f"Activity {ac2} now using")
                Activity7()
                continue
            elif ac2 == "8":
                print(f"Selected Number: {ac2}")
                print(f"Activity {ac2} now using")
                Activity8()
                continue
            elif ac2 == "9":
                print(f"Selected Number: {ac2}")
                print(f"Activity {ac2} now using")
                Activity9()
                continue
            elif ac2 == "10":
                print(f"Selected Number: {ac2}")
                print(f"Activity {ac2} now using")
                Activity10()
                continue
            elif ac2 == "m":
                print("Menu..")
            else:
                print("Error Choose again")
                continue
        elif act1 == 3:
            print("Welcome to my Activities(11-15)")
            print("11 = Activity6\n12 = Activity7\n13 = Activity8\n14 = Activity9\n15 = Activity10\nM - Menu")
            ac3 = input("Choose: ").lower()
            if ac3 == "11":
                print(f"Selected Number: {ac3}")
                print(f"Activity {ac3} now using")
                Activity11()
                continue
            elif ac3 == "12":
                print(f"Selected Number: {ac3}")
                print(f"Activity {ac3} now using")
                Activity12()
                continue
            elif ac3 == "13":
                print(f"Selected Number: {ac3}")
                print(f"Activity {ac3} now using")
                Activity13()
                continue
            elif ac3 == "14":
                print(f"Selected Number: {ac3}")
                print(f"Activity {ac3} now using")
                Activity14()
                continue
            elif ac3 == "15":
                print(f"Selected Number: {ac3}")
                print(f"Activity {ac3} now using")
                Activity15()
                continue
            elif ac3 == "m":
                print("Menu..")
            else:
                print("Error Choose again")
                continue
        elif act1 == 4:
            print("Welcome to my Activities(16-20)")
            print("16 = Activity16\n17 = Activity17\n18 = Activity18\n19 = Activity19\n20 = Activity20\nM - Menu")
            ac4 = input("Choose: ").lower()
            if ac4 == "16":
                print(f"Selected Number: {ac4}")
                print(f"Activity {ac4} now using")
                Activity16()
                continue
            elif ac4 == "17":
                print(f"Selected Number: {ac4}")
                print(f"Activity {ac4} now using")
                Activity17()
                continue
            elif ac4 == "18":
                print(f"Selected Number: {ac4}")
                print(f"Activity {ac4} now using")
                Activity18()
                continue
            elif ac4 == "19":
                print(f"Selected Number: {ac4}")
                print(f"Activity {ac4} now using")
                Activity19()
                continue
            elif ac4 == "20":
                print(f"Selected Number: {ac4}")
                print(f"Activity {ac4} now using")
                Activity20()
                continue
            elif ac4 == "m":
                print("Menu..")
            else:
                print("Error Choose again")
                continue
        elif act1 == 5:
            print("Welcome to my Activities(16-20)")
            print("21 = Activity21\n22 = Activity22\n23 = Activity23\n24 = Activity24\n24.1 = Activity24.1\n25 = Activity25\n25.1 = Activity25.1\nM - Menu")
            ac5 = input("Choose: ").lower()
            if ac5 == "21":
                print(f"Selected Number: {ac5}")
                print(f"Activity {ac5} now using")
                Activity21()
                continue
            elif ac5 == "22":
                print(f"Selected Number: {ac5}")
                print(f"Activity {ac5} now using")
                Activity22()
                continue
            elif ac5 == "23":
                print(f"Selected Number: {ac5}")
                print(f"Activity {ac5} now using")
                Activity23()
                continue
            elif ac5 == "24":
                print(f"Selected Number: {ac5}")
                print(f"Activity {ac5} now using")
                Activity24()
                continue
            elif ac5 == "24.1":
                print(f"Selected Number: {ac5}")
                print(f"Activity {ac5} now using")
                Activity241()
                continue
            elif ac5 == "25":
                print(f"Selected Number: {ac5}")
                print(f"Activity {ac5} now using")
                activity25()
                continue
            elif ac5 == "25.1":
                print(f"Selected Number: {ac5}")
                print(f"Activity {ac5} now using")
                Activity251()
                continue
            elif ac5 == "m":
                print("Menu..")
            else:
                print("Error Choose again")
                continue
        continue

#Code Challenge
    elif n == "2": 
        print("Welcome to my Code Challenges")
        print("1 = CChallenge(1-5)\n2 = CChallenge(6-10)\n3 = CChallenge(11-15)")
        np = input("Choose: ")
        if np == "1":
            print("Welcome to my Code Challenges(1-5)")
            print("1 = CChallenge1\n2 = CChallenge2\n3 = CChallenge3\n4 = CChallenge4\n5 = CChallenge5\nM = Menu")
            cc1 = input("Choose: ").lower()
            if cc1 == "1":
                print(f"Selected Number: {cc1}")
                print(f"Code Challenge {cc1} now using")
                ccode1()
                continue
            elif cc1 == "2":
                print(f"Selected Number: {cc1}")
                print(f"Code Challenge {cc1} now using")
                ccode2()
                continue
            elif cc1 == "3":
                print(f"Selected Number: {cc1}")
                print(f"Code Challenge {cc1} now using")
                ccode3()
                continue
            elif cc1 == "4":
                print(f"Selected Number: {cc1}")
                print(f"Code Challenge {cc1} now using")
                ccode4()
                continue
            elif cc1 == "5":
                print(f"Selected Number: {cc1}")
                print(f"Code Challenge {cc1} now using")
                ccode5()
                continue
            elif cc1 == "m":
                print("Menu..")
            else:
                print("Error Try again")
                continue
        elif np == "2":
            print("Welcome to my Code Challenges(6-10)")
            print("6 = CChallenge6\n7 = CChallenge7\n8 = CChallenge8\n9 = CChallenge9\n10 = CChallenge10\nM = Menu")
            cc2 = input("Choose: ").lower()
            if cc2 == "6":
                print(f"Selected Number: {cc2}")
                print(f"Code Challenge {cc2} now using")
                ccode6()
                continue
            elif cc2 == "7":
                print(f"Selected Number: {cc2}")
                print(f"Code Challenge {cc2} now using")
                ccode7()
                continue
            elif cc2 == "8":
                print(f"Selected Number: {cc2}")
                print(f"Code Challenge {cc2} now using")
                ccode8()
                continue
            elif cc2 == "9":
                print(f"Selected Number: {cc2}")
                print(f"Code Challenge {cc2} now using")
                ccode9()
                continue
            elif cc2 == "10":
                print(f"Selected Number: {cc2}")
                print(f"Code Challenge {cc2} now using")
                ccode10()
                continue
            elif cc2 == "m":
                print("Menu..")
            else:
                print("Error Try again")
                continue
        elif np == "3":
            print("Welcome to my Code Challenges(6-10)")
            print("11 = CChallenge11\n12 = CChallenge12\n13 = CChallenge13\n14 = CChallenge14\n15 = CChallenge15\nM = Menu")
            cc3 = input("Choose: ").lower()
            if cc3 == "11":
                print(f"Selected Number: {cc3}")
                print(f"Code Challenge {cc3} now using")
                ccode11()
                continue
            elif cc3 == "12":
                print(f"Selected Number: {cc3}")
                print(f"Code Challenge {cc3} now using")
                ccode12()
                continue
            elif cc3 == "13":
                print(f"Selected Number: {cc3}")
                print(f"Code Challenge {cc3} now using")
                ccode13()
                continue
            elif cc3 == "14":
                print(f"Selected Number: {cc3}")
                print(f"Code Challenge {cc3} now using")
                ccode14()
                continue
            elif cc3 == "15":
                print(f"Selected Number: {cc3}")
                print(f"Code Challenge {cc3} now using")
                ccode15()
                continue
            elif cc3 == "m":
                print("Menu..")
            else:
                print("Error Try again")
                continue
        continue
    elif n == "p".lower():
        print("Exiting.....")
        print("(Exit or Continue)")
        ex = input(":").lower()
        if ex == "continue":
            print("Welcome")
            continue
        elif ex == "exit":
            print("Thank You For Using my Ai")
            print("Bye bye")
            break
    else:
        print("Error,Choose only between choices")
        continue