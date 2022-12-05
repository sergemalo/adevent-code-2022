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


class ElfGroup:
    def __init__(self):
        self.rucksacks = []
        self.badge = 0

    def findBadge(self):
        if (len(self.rucksacks) != 3):
            raise ("There is not 3 Rucksacks in this group!")
        for i0 in self.rucksacks[0].oriLine:
            for i1 in self.rucksacks[1].oriLine:
                for i2 in self.rucksacks[2].oriLine:
                    if ((i0 == i1) and (i0 == i2)):
                        print (i0)
                        return i0

        #badgeFound = False
        #rucksack0Idx = 0
        #while ((badgeFound == False) && (rucksack0Idx < len(rucksacks[0].oriLine))):
        #    item0 = rucksacks[0].oriLine[0]

        return "A"

f = open("dec3-dataset.txt", "rt")
lineCount = 0

rucksackList = []
totalPriorities = 0
errorFoundCount = 0
curElfGroup = ElfGroup()
curRucksackIdxOfGroup = 0
elfGroups = []
badgesPriorities = 0

for line in f:
    line = line.strip()
    lineCount = lineCount + 1
    print(line)
    curRucksack = rucksack(line)
    if (curRucksack.errorFound):
        errorFoundCount = errorFoundCount + 1
        totalPriorities = totalPriorities + priority(curRucksack.errorItem)
    curElfGroup.rucksacks.append(copy.deepcopy(curRucksack))
    curRucksackIdxOfGroup = curRucksackIdxOfGroup + 1
    if (curRucksackIdxOfGroup == 3):
        badgesPriorities = badgesPriorities + priority(curElfGroup.findBadge())
        elfGroups.append(copy.deepcopy(curElfGroup))
        curElfGroup = ElfGroup()
        curRucksackIdxOfGroup = 0
    rucksackList.append(copy.deepcopy(curRucksack))

f.close()


print("Total of lines: " + str(lineCount))
print("Total of Rucksacks: " + str(len(rucksackList)))
print("Total of Errors: " + str(errorFoundCount))
print("Total of Priorities: " + str(totalPriorities))
print("Total of Groups: " + str(len(elfGroups)))
print("Total of Priorities of badges: " + str(badgesPriorities))
print ("Priority of a: " + str(priority("a")))
print ("Priority of z: " + str(priority("z")))
print ("Priority of A: " + str(priority("A")))
print ("Priority of Z: " + str(priority("Z")))
