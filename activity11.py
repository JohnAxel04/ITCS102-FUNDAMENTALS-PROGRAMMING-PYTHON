#Temperature checker

tmp = eval(input("what temp is it now? "))

if tmp <= 0:
    print("the temp is freaking cold")
elif tmp >= 1 and tmp <= 20:
    print("The temp is cold")
elif tmp >= 21 and tmp <= 30:
    print("The temp is lookwarm")
elif tmp >= 31 and tmp <= 40:
    print("The temp is warm")
elif tmp >= 41 and tmp <= 50:
    print("The temp is hot")
elif tmp >= 51:
    print("The temp is boiling hot")
else:
    print("error")