import copy

class Elf:
    def __init__(self):
        self.snacks = []

    def calories(self):
        totalCalories = 0
        for c in self.snacks:
            totalCalories = totalCalories + c
        return totalCalories

f = open("dec1-dataset.txt", "rt")
lineCount = 0
elfCount = 0
curElf = Elf()
curElfTotalCal = 0
maxCalForOneElf = 0

elfList = []
for line in f:
    line = line.strip()
    lineCount = lineCount + 1
    if line != "":
        curElfTotalCal = curElfTotalCal + int(line)
        curElf.snacks.append(int(line))
    else:
        elfList.append(copy.deepcopy(curElf))
        curElf.snacks.clear()
        elfCount = elfCount + 1
        if curElfTotalCal > maxCalForOneElf:
            maxCalForOneElf = curElfTotalCal
            print("New Max Calories: " + str(maxCalForOneElf))
        curElfTotalCal = 0
    print(line)

f.close()


print("Total of lines: " + str(lineCount))
print("Total of Elfs: " + str(elfCount))
print("Total of Elfs: " + str(len(elfList)))
print("Elf with Max food has: " + str(maxCalForOneElf) + " calories")

elfList.sort(reverse=True, key=Elf.calories)

print (elfList[0].snacks)
print (elfList[1].snacks)
print (elfList[2].snacks)
print (str(elfList[0].calories()))
print (str(elfList[1].calories()))
print (str(elfList[2].calories()))
top3TotalCal = 0
for elf in elfList[0:3]:
    top3TotalCal = top3TotalCal + elf.calories()
print ("Total calories for top 3 Elfs: " + str(top3TotalCal))
