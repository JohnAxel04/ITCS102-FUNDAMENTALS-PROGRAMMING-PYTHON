#Anime list
#Using list and while loop
print("Anime Title List")

anime = [] #empty list
mn = True   

while mn == True:
    num = input("Put a Title of an Anime: ")
    print("Anime Added to the List")
    anime.append(num) #all title that put will go to the list
    if num == "exit": #stopper
        print("All done")
        anime.pop() #the word exit will be remove
        break

print(f"All anime in your list {anime}") #will print all the anime u putted
