from array import *

class Tree:
    def __init__(self, height):
        self.height = height
        self.visible = False

treeGrid = [[]]

def treeVisible(index, list):
    if index == 0:
        return True
    if index == (len(list) - 1):
        return True



f = open("dec8-dataset.txt", "rt")
lineCount = 0
for line in f:
    line = line.strip()
    print(line)

    for i in line:
        t = Tree(int(i))
        treeGrid[lineCount].append(t)
    treeGrid.append([])
    lineCount = lineCount + 1

f.close()

rIdx = 0
for r in treeGrid:
    for c in r:
        print("H:" + str(c.height))

print("Total of lines: " + str(lineCount))
