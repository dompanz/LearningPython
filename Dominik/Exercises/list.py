import random
# generate random list
rndlist = random.sample(range(15), 10)
outlist = []
print(rndlist)
num = int(input("Homy give me the number you please: "))
for element in rndlist:
	if(element < num):
		outlist.append(element)
print(outlist)