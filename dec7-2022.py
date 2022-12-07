import re

maxDirSize = 10000
totalSizeOfDirs = 0

f = open("dec7-dataset.txt", "rt")
lineCount = 0

for line in f:
    line = line.strip()
    lineCount = lineCount + 1
    print(line)

f.close()
print("Total of lines: " + str(lineCount))
print("Total size of dirs with less than " + str(maxDirSize) + ": " + str(totalSizeOfDirs))
