import copy

def priority(item):
    if (ord(item[0]) > 96):
        return ord(item[0]) - 96
    else:
        return ord(item[0]) - 38

class rucksack:
    def __init__(self, initLine):
        self.oriLine = initLine
        self.errorFound = False
        self.errorItem = ""
        if ((len(self.oriLine) % 2)):
            raise ("Odd line length: " + len(self.oriLine))
        self.compartItemsCount = int(len(self.oriLine)/2)
        self.comparts = [self.oriLine[0:self.compartItemsCount], self.oriLine[self.compartItemsCount:]]
        print(self.comparts)
        self.findError()
        if (self.errorFound):
            print ("Error: " + self.errorItem)

    def findError(self):
        for l in self.comparts[0]:
            for n in self.comparts[1]:
                if (l == n):
                    self.errorFound = True
                    self.errorItem = l



f = open("dec3-dataset.txt", "rt")
lineCount = 0

rucksackList = []
totalPriorities = 0
errorFoundCount = 0
for line in f:
    line = line.strip()
    lineCount = lineCount + 1
    print(line)
    curRucksack = rucksack(line)
    if (curRucksack.errorFound):
        errorFoundCount = errorFoundCount + 1
        totalPriorities = totalPriorities + priority(curRucksack.errorItem)
    rucksackList.append(copy.deepcopy(curRucksack))

f.close()


print("Total of lines: " + str(lineCount))
print("Total of Rucksacks: " + str(len(rucksackList)))
print("Total of Errors: " + str(errorFoundCount))
print("Total of Priorities: " + str(totalPriorities))
print ("Priority of a: " + str(priority("a")))
print ("Priority of z: " + str(priority("z")))
print ("Priority of A: " + str(priority("A")))
print ("Priority of Z: " + str(priority("Z")))
