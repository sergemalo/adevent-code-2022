import re

def hasDupplicatedLetter(str):
    if (len(str) < 2):
        return False;
    for i in range (len(str)-1):
        for j in range (i+1, len(str)):
            #print (str[i] + ";" + str[j])
            if (str[i] == str[j]):
                return True
    return False

def findMarkerAndFirstIdx(buffer, length):
    markerFound = False
    curIdx = 0
    marker = ""
    while ((not markerFound) and (curIdx < len(buffer))):
        #print (str(buffer[curIdx]))
        while (len(marker) < length):
            marker = marker + buffer[curIdx]
            curIdx = curIdx + 1
        #print (marker)
        while (hasDupplicatedLetter(marker)):
            marker = marker[1:len(marker)]
        #print (marker)
        if (len(marker) == length):
            markerFound = True
    if (not markerFound):
        curIdx = 0
        marker = ""
    return (marker, curIdx)


f = open("dec6-dataset.txt", "rt")
lineCount = 0
marker = ""
SOMIdx = 0
SOM = ""
firstMarkerIdx = 0

for line in f:
    line = line.strip()
    lineCount = lineCount + 1
    print(line)
    marker, firstMarkerIdx = findMarkerAndFirstIdx(line, 4)
    SOM, SOMIdx = findMarkerAndFirstIdx(line, 14)

f.close()
print("Total of lines: " + str(lineCount))
print("Marker: " + marker + "; First Index = " + str(firstMarkerIdx))
print("Start Of Message: " + SOM + "; First Index = " + str(SOMIdx))
