# Get the User Input
name = input("Give me your name baby: ")
date = input("And now your Birthdate " + name + " (with format DD.MM.YYYY): ")
year = int(date[-4:])
turnhundred = year + 100;
print("Buo you turn 100 on " +date[:-4]+ str(turnhundred))