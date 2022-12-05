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

for line in f:
    line = line.strip()
    lineCount = lineCount + 1
    print(line)
    if ((len(line) > 1) and (line[0] == "1")):
        print ("Parsing Init Stock done!")
        parsingInitStockDone = True
    if ((len(line) > 0) and parsingInitStockDone):
        #move 3 from 2 to 5
        pattern = "^move (\d+) from (\d+) to (\d+)$"
        result = re.match(pattern, line)
        if (result):
            print ("A" + result.group(1))
        else:
            print ("CACA")
            raise ("Unable to parse: " + line)

f.close()

print("Total of lines: " + str(lineCount))
