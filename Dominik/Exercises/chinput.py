import datetime

# Get the current date
now = datetime.datetime.now()
# Get the User Input
name = input("Give me your name baby: ")
#date = input("And now your Birthdate " + name + " (with format DD.MM.YYYY): ")
age = int(input("How old are you right now, lil homy?: "))
# Calculate the deathyear
#year = int(date[-4:])
turnhundred = now.year - age + 100;
# Print it
print("Buo you turn 100 in fucking " + str(100-age) + " years hohohoo" +
	"\nYou will be 100 in the Year " + str(turnhundred))
