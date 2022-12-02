def gameScore(other, mine):
    score = 0
    if (mine == "X"):
        if (other == "A"):
            score = 1 + 3
        elif (other == "B"):
            score = 1 + 0
        elif (other == "C"):
            score = 1 + 6
    if (mine == "Y"):
        if (other == "A"):
            score = 2 + 6
        elif (other == "B"):
            score = 2 + 3
        elif (other == "C"):
            score = 2 + 0
    if (mine == "Z"):
        if (other == "A"):
            score = 3 + 0
        elif (other == "B"):
            score = 3 + 6
        elif (other == "C"):
            score = 3 + 3
    return score


f = open("dec2-dataset.txt", "rt")
lineCount = 0
totalScore = 0
for line in f:
    lineCount = lineCount + 1
    line = line.strip()
    print(line)
    other = line[0]
    mine = line[2]
    totalScore = totalScore + gameScore(other, mine)
    print (str(gameScore(other, mine)))

f.close()

print("Total of lines: " + str(lineCount))
print("Total Score: " + str(totalScore))
