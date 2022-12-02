import sys

f = open("dec1-dataset.txt", "rt")
lineCount = 0
elfCount  = 0
curFood = 0
maxFood = 0
for line in f:
    line = line.strip()
    lineCount = lineCount + 1
    if (line != ""):
        curFood = curFood + int(line)
    else:
        elfCount = elfCount +1
        if (curFood > maxFood):
            maxFood = curFood
            print("New Max Food: " + str(maxFood))
        curFood = 0
    print(line)

print ("Total of lines: " + str(lineCount))
print ("Total of Elf: " + str(elfCount))
print ("Elf with Max food has: " + str(maxFood) + " calories")
f.close()
