#Anime list
#Using list and while loop
print("Anime Title List")

anime = [] #empty list
mn = True   

while mn == True:
    num = input("Put a Title of an Anime: ")
    print("Anime Added to the your Anime List")
    anime.append(num) #all title that put will go to the list
    if num == "exit": #stopper
        print("All done,You are now exiting!! ")
        anime.pop()
        break

print(f"Here All the Title of your Anime: ") #will print all the anime u putted
for r in anime:
    print(f"- {r}")