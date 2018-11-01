#Character Input
name = input("Wie heißt du Buo? Sag es: ")
print("So, so du bist also "+ name + " <3!")
birth = input("Und wann hat deine Mudda dich geworfen? Sag es (TT:MM:JJJJ): ")
print("Perfekt! " + birth + " der Tag ist ja schon ewig her, du alte Sau.")
age = int(input("Jetzt sag mir noch wie alt du bist: "))
year = int(birth[6:10])
lifetime = (100 - age)
deathyear = 100 + year
print("So du alter Zigeuner, du hast noch " + str(lifetime) + " Jahre bis du am " + birth[0:6] + str(deathyear) +" tot umfällst.")
