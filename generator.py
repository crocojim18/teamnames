import random

def titleCase(string):
	toRet = []
	for i in string.split(" "):
		if "a" <= i[0] <= "z":
			toRet.append(i[0].upper()+i[1:])
		else:
			toRet.append(i)
	return " ".join(toRet)

places = open("places.txt",'r',encoding="utf-8")
nouns = open("nouns.txt",'r',encoding="utf-8")

placelist = places.readlines()
nounlist = nouns.readlines()

for i in range(10):
	choosePlace = placelist[random.randrange(0,len(placelist))].strip()
	chooseNoun = nounlist[random.randrange(0,len(nounlist))].strip()

	print(titleCase("The {} {}".format(choosePlace, chooseNoun)))

places.close()
nouns.close()
