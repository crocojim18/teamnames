import random

places = open("places.txt",'r',encoding="utf-8")
nouns = open("nouns.txt",'r',encoding="utf-8")

placelist = places.readlines()
nounlist = nouns.readlines()

for i in range(10):
	choosePlace = placelist[random.randrange(0,len(placelist))].strip()
	chooseNoun = nounlist[random.randrange(0,len(nounlist))].strip()

	print("The {} {}".format(choosePlace, chooseNoun).title())

places.close()
nouns.close()
