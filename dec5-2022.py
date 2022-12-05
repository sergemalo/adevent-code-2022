import re

class Stack:
    def __init__(self):
        self.crates = []

    def push(self, crate):
        self.cartes.append(crate)

    def pop(self):
        self.cartes.append("")


f = open("dec5-dataset.txt", "rt")
lineCount = 0

parsingInitStockDone = False

allStacks = {}
allStacks[1] = ["N", "D", "M", "Q", "B", "P", "Z"]
allStacks[2] = ["C", "L", "Z", "Q", "M", "D", "H", "V"]
allStacks[3] = ["Q", "H", "R", "D", "V", "F", "Z", "G"]
allStacks[4] = ["H", "G", "D", "F", "N"]
allStacks[5] = ["N", "F", "D"]
allStacks[6] = ["D", "Q", "V", "Z", "F", "B", "T"]
allStacks[7] = ["Q", "M", "T", "Z", "D", "V", "S", "H"]
allStacks[8] = ["M", "G", "F", "P", "N", "Q"]
allStacks[9] = ["B", "W", "R", "M"]

for line in f:
    line = line.strip()
    lineCount = lineCount + 1
    print(line)
    if ((len(line) > 1) and (line[0] == "1")):
        print ("Parsing Init Stock done!")
        parsingInitStockDone = True
    elif ((len(line) > 0) and parsingInitStockDone):
        #move 3 from 2 to 5
        pattern = "^move (\d+) from (\d+) to (\d+)$"
        result = re.match(pattern, line)
        if (result):
            print ("A" + result.group(1))
            src = int(result.group(2))
            dst = int(result.group(3))
            loops = int(result.group(1))
            for x in range(1, loops + 1):
                allStacks[dst].append(allStacks[src].pop())
        else:
            print ("CACA")
            raise Exception("Unable to parse: " + line)

f.close()

print("Total of lines: " + str(lineCount))
finalStrig = ""
for k in allStacks.keys():
    print ("Key: " + str(k))
    finalStrig += (allStacks[k][len(allStacks[k]) - 1])
    print ("Stack top: " + allStacks[k][len(allStacks[k]) - 1])
    
print ("Final string: " + finalStrig)
