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
				if index == 7:
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
	for line in data:
		if line[0] == animal:
			print("\nname: %s" % (line[0]))
			print("hair: %s" % (line[1]))
			print("feathers: %s" % (line[2]))
			print("eggs: %s" % (line[3]))
			print("predator: %s" % (line[4]))
			print("venomous: %s" % (line[5]))
			print("fins: %s" % (line[6]))
			print("number of legs: %s" % (line[7]))
			print("tail: %s" % (line[8]))
			print("dangerous: %s" % (line[9]))
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
	print(info)
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