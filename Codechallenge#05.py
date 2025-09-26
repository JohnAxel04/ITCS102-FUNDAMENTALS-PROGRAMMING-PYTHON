#My Anime List
#Different type of Anime
#Duration of Anime

print("Welcome To my Anime library")
print("Anime list Recommendation")
print("what kind of anime")
print("1-ISEKAI")
print("2-COMEDY")
print("3-FANTACY")
print("4-ACTION")
menu = int(input("What kind of Anime you like(1,2,3,4,): "))

#Isekaiiiiiiiiiiiii

if menu == 1:
	selected = "ISEKAI"
	print("Anime :", selected)
	long = input("Range (Long or Short): ")

#longggggggg

	if long.lower() == "long":
		print("Size:", long)
		year = eval(input("What year(2000,2010,2020): "))

		if year == 2000:
			print("Year: ", year)
			print("I recommend Anime for",selected,"range of",long,"Year",year, "\n-The Twelve Kingdoms Is Rightfully Regarded as a Cult Classic of Isekai \n-MÄR Embraces the Best Shonen Clichés \n-Kiba Is Unexpectedly Bleak for a Card Game Isekai Adventure")
		
		elif year == 2010:
			print("Year: ", year)
			print("I recommend Anime for",selected,"range of",long,"Year",year,"\n-Magi: The Labyrinth of Magic\n-Re:Zero – Starting Life in Another World\n-Sword Art Online")
		
		elif year == 2020:
			print("Year: ", year)
			print("I recommend Anime for",selected,"range of",long,"Year",year,"\n-Konosuba\n-That Time I Got Reincarnated as a Slime\n-Jobless Reincarnation: Mushoku Tensei")
	
		else:
			print("Thank You so Much")

#SHortttttt

	if long.lower() == "short":
		print("Size:", long)
		year = eval(input("What year(2000,2010,2020): "))

		if year == 2000:
			print("Year: ", year)
			print("I recommend Anime for",selected,"range of",long,"Year",year, "\n-Dual! Parallel Trouble Adventure\n-Now and Then, Here and There\n-Haibane Renmei")
		
		elif year == 2010:
			print("Year: ", year)
			print("I recommend Anime for",selected,"range of",long,"Year",year,"\n-No Game No Life\n-Problem Children Are Coming from Another World, Aren’t They?\n-Gate: Jieitai Kanochi nite, Kaku Tatakaeri")
		elif year == 2020:
			print("Year: ", year)
			print("I recommend Anime for",selected,"range of",long,"Year",year,"\n-Wise Man’s Grandchild (Kenja no Mago)\n-Tsukimichi: Moonlit Fantasy (Season 2)\n-How a Realist Hero Rebuilt the Kingdom")
		else:
			print("Error Put Year")
	else:
		print("Error, put Long or Short")

#COmedyyyyyyy

elif menu == 2:
	selec = "COMEDY"
	print("Anime: ",selec)
	longe = input("Range (Long or Short): ")

#Longggg

	if longe.lower() == "long":
		print("Size:", longe)
		years = eval(input("What year(2000,2010,2020): "))

		if years == 2000:
			print("Year: ", years)
			print("I recommend Anime for",selec,"range of",longe,"Year",years, "\n-Gintama\n-School Rumble\n-One Piece")
		elif years == 2010:
			print("Year: ", years)
			print("I recommend Anime for",selec,"range of",longe,"Year",years, "\n-Fairy Tail\n-Sket Dance\n-Assassination Classroom")
		elif years == 2020:
			print("Year: ", years)
			print("I recommend Anime for",selec,"range of",longe,"Year",years, "\n-KonoSuba: God’s Blessing on This Wonderful World!\n-Uzaki-chan Wants to Hang Out!\n-Komi Can’t Communicate")
		else:
			print("error put year")

#Shorttttt
	
	elif longe.lower() == "short":
		print("Size:", longe)
		years = eval(input("What year(2000,2010,2020): "))

		if years == 2000:
			print("Year: ", years)
			print("I recommend Anime for",selec,"range of",longe,"Year",years, "\n-Excel Saga\n-Azumanga Daioh\n-Pani Poni Dash!")

		elif years == 2010:
			print("Year: ", years)
			print("I recommend Anime for",selec,"range of",longe,"Year",years, "\n-Nichijou (My Ordinary Life)\n-Isekai Quartet\n-Asobi Asobase")
		elif years == 2020:
			print("Year: ", years)
			print("I recommend Anime for",selec,"range of",longe,"Year",years, "\n-Komi Can’t Communicate\n-My Senpai is Annoying\n-Spy × Family")
		else:
			print("error put year")	
	else:
		print("error put long or short")

elif menu == 3:
	sel = "Adventure"
	print("Anime: ",sel)
	longes = input("Range (Long or Short): ")
	
	if longes.lower() == "long":
		print("Size:", longes)
		yearsw = eval(input("What year(2000,2010,2020): "))

		if yearsw == 2000:
			print("Year: ", yearsw)
			print("I recommend Anime for",sel,"range of",longes,"Year",yearsw, "\n-One Piece\n-Naruto\n-Bleach")
		elif yearsw == 2010:
			print("Year: ", yearsw)
			print("I recommend Anime for",sel,"range of",longes,"Year",yearsw, "\n-Hunter × Hunter\n-Boruto: Naruto Next Generations\n-Sword Art Online")
		elif yearsw == 2020:
			print("Year: ", yearsw)
			print("I recommend Anime for",sel,"range of",longes,"Year",yearsw, "\n-Black Clover\n-Dragon Quest: The Adventure of Dai\n-That Time I Got Reincarnated as a Slime")
		else:
			print("error put year")

	elif longes.lower() == "short":
		print("Size:", longes)
		yearsw = eval(input("What year(2000,2010,2020): "))

		if yearsw == 2000:
			print("Year: ", yearsw)
			print("I recommend Anime for",sel,"range of",longes,"Year",yearsw, "\n-Scrapped Princess\n-Wolf’s Rain\n-Samurai Champloo")
		elif yearsw == 2010:
			print("Year: ", yearsw)
			print("I recommend Anime for",sel,"range of",longes,"Year",yearsw, "\n-Made in Abyss\n-No Game No Life\n-Noragami")	
		elif yearsw == 2020:
			print("Year: ", yearsw)
			print("I recommend Anime for",sel,"range of",longes,"Year",yearsw, "\n-Jobless Reincarnation: Mushoku Tensei\n-Ranking of Kings (Ousama Ranking)\n-Somali and the Forest Spirit")
		else:
			print("error put year")

elif menu == 4:
	sell = "Action"
	print("Anime: ",sell)
	longest = input("Range (Long or Short): ")
	
	if longest.lower() == "long":
		print("Size:", longest)
		yearsp = eval(input("What year(2000,2010,2020): "))
	
		if yearsp == 2000:
			print("Year: ", yearsp)
			print("I recommend Anime for",sell,"range of",longest,"Year",yearsp, "\n-Fullmetal Alchemist\n-D.Gray-man\n-Zatch Bell! (Konjiki no Gash Bell!!)")
		elif yearsp == 2010:
			print("Year: ", yearsp)
			print("I recommend Anime for",sell,"range of",longest,"Year",yearsp, "\n-JoJo’s Bizarre Adventure\n-Attack on Titan\n-World Trigger")
		elif yearsp == 2020:
			print("Year: ", yearsp)
			print("I recommend Anime for",sell,"range of",longest,"Year",yearsp, "\n-My Hero Academia\n-Bleach: Thousand-Year Blood War\n-Demon Slayer")
		else:
			print("error put year")
	elif longest.lower() == "short":
		print("Size:", longest)
		yearsp = eval(input("What year(2000,2010,2020): "))

		if yearsp == 2000:
			print("Year: ", yearsp)
			print("I recommend Anime for",sell,"range of",longest,"Year",yearsp, "\n-Black Lagoon\n-Afro Samurai\n-Gungrave")
		elif yearsp == 2010:
			print("Year: ", yearsp)
			print("I recommend Anime for",sell,"range of",longest,"Year",yearsp, "\n-Akame ga Kill!\n-Parasyte: The Maxim\n-Black Bullet")
		
		elif yearsp == 2020:
			print("Year: ", yearsp)
			print("I recommend Anime for",sell,"range of",longest,"Year",yearsp, "\n-Jujutsu Kaisen\n-Chainsaw Man\n-Tower of God")
		else:
			print("error put year")
	else:
		print("error put long or short")
else:
	print("error \nplease select 1,2,3,4")
		
	
	
		


		
		

			
		
		
	




