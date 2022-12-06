import re

def findMarkerAndFirstIdx(buffer):
    markerFound = False
    curIdx = 0
    marker = ""
    while ((not markerFound) and (curIdx < len(buffer))):
        print (str(buffer[curIdx]))
        while (len(marker) < 4):
            marker = marker + buffer[curIdx]
            curIdx = curIdx + 1
        if (cur char found in marker):
            marker = marker + buffer[curIx]
        else:
            marker = maker[
        curIdx = curIdx + 1
    if (not markerFound):
        curIdx = 0
        marker = ""
    return (marker, curIdx)


f = open("dec6-dataset.txt", "rt")
lineCount = 0
marker = ""
firstMarkerIdx = 0

for line in f:
    line = line.strip()
    lineCount = lineCount + 1
    print(line)
    marker, firstMarkerIdx = findMarkerAndFirstIdx(line)

f.close()
print("Total of lines: " + str(lineCount))
print("Marker: " + marker + "; First Index = " + str(firstMarkerIdx))
