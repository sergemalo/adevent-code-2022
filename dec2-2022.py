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


def myPlay(other, cmd):
    if (cmd == "X"):
        if (other == "A"):
            mine = "Z"
        elif (other == "B"):
            mine = "X"
        elif (other == "C"):
            mine = "Y"
    if (cmd == "Y"):
        if (other == "A"):
            mine = "X"
        elif (other == "B"):
            mine = "Y"
        elif (other == "C"):
            mine = "Z"
    if (cmd == "Z"):
        if (other == "A"):
            mine = "Y"
        elif (other == "B"):
            mine = "Z"
        elif (other == "C"):
            mine = "X"
    return mine



f = open("dec2-dataset.txt", "rt")
lineCount = 0
totalScore = 0
for line in f:
    lineCount = lineCount + 1
    line = line.strip()
    print(line)
    other = line[0]
    mine = line[2]
    totalScore = totalScore + gameScore(other, myPlay(other, mine))
    print (str(gameScore(other, myPlay(other, mine))))

f.close()

print("Total of lines: " + str(lineCount))
print("Total Score: " + str(totalScore))
