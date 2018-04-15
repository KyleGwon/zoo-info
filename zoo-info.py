def getData(data):
	returnList = []
	for line in data:
		line = line.strip("\n")
		pieces = line.split(",")
		returnList.append(pieces)
	return returnList
def changeNums(data):
	oldData = getData(data)
	newData = []
	for line in oldData:
		animalData = []
		danger = 0
		for index in range(len(line)):
			if index == 4:
				if line[4] == "1":
					danger += 1
			elif index == 5:
				if line[5] == "1":
					danger += 1
			if line[index].isalpha():
				animalData.append(line[index])
			else:
				if index == 13:
					animalData.append(line[index])
				else:
					if line[index] == "1":
						animalData.append("True")
					elif line[index] == "0":
						animalData.append("False")
		if danger == 0:
			animalData.append("low")
		elif danger == 1:
			animalData.append("medium")
		else:
			animalData.append("high")
		newData.append(animalData)
	return newData
def getInfo(data):
	animal = input("search for: ").lower()
	firstIndex = 0
	lastIndex = len(data) - 1
	while firstIndex <= lastIndex:
		middleIndex = (firstIndex + lastIndex)//2
		print(data[middleIndex][0])
		print(animal)
		if data[middleIndex][0] == animal:
			animalIndex = middleIndex
			break
		else:
			if animal < data[middleIndex][0]:
				lastIndex -= 1
			else:
				firstIndex += 1
	try:
		print("\nname: %s" % (data[animalIndex][0]))
		print("hair: %s" % (data[animalIndex][1]))
		print("feathers: %s" % (data[animalIndex][2]))
		print("eggs: %s" % (data[animalIndex][3]))
		print("milk: %s" % (data[animalIndex][4]))
		print("airborne: %s" % (data[animalIndex][5]))
		print("aquatic: %s" % (data[animalIndex][6]))
		print("predator: %s" % (data[animalIndex][7]))
		print("toothed: %s" % (data[animalIndex][8]))
		print("backbone: %s" % (data[animalIndex][9]))
		print("breathes: %s" % (data[animalIndex][10]))
		print("venomous: %s" % (data[animalIndex][11]))
		print("fins: %s" % (data[animalIndex][12]))
		print("number of legs: %s" % (data[animalIndex][13]))
		print("tail: %s" % (data[animalIndex][14]))
		print("domestic: %s" % (data[animalIndex][15]))
		print("catsize: %s" % (data[animalIndex][16]))
		print("type: %s" % (data[animalIndex][17]))
		print("danger: %s" % (data[animalIndex][len(data[animalIndex]) - 1]))
	except:
		print("Error: Animal not in database")
def getLegs(data):
	animals = []
	minLegs = int(input("Minimum number of legs: "))
	maxLegs = int(input("Maximum number of legs: "))
	print("\nAnimal # legs\n------ ------")
	for line in data:
		if minLegs < int(line[7]) < maxLegs:
			print(line[0], line[7])
def getDangerous(data):
	dangerous = []
	for line in data:
		if line[len(line)-1] == "high":
			dangerous.append(line[0])
	for animal in dangerous:
		print(animal)
def main():
	file = "animals.data"
	data = open(file, "r")
	info = changeNums(data)
	print("======== Information on Animals at the Zoo ========")
	while True:
		print("\n===================================================")
		var = input("(1) Animal Name (2) Number of legs (3) Quit : ")
		if var == "1":
			getInfo(info)
		elif var == "2":
			getLegs(info)
		elif var == "3":
			break
		else:
			print("Error: invalid input")
	print("\n===================================================")
	print("Warning! The following animals are very dangerous,\ndo not attempt to hug them at the zoo:")
	getDangerous(info)
	print("\nHave a fun day at the zoo!")
main()
