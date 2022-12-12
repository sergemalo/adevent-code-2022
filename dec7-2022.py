import re

maxDirSize = 100000
FSSizeTotal = 70000000
freeSpaceNeeded = 30000000
fileSystemSize = 0

def f1(p1):
    p1 += 1

class c1:
    def __init__(self):
        self.m1 = 0

    def f2(self, p1):
        self.m1 += 1
        p1 += 1
        self.f3(self.m1)
        return p1

    def f3(self, p1):
        p1 += 1

p1 = 0
print ("p1 = " + str(p1))
f1(p1)

o1 = c1()
p1 = 0
print ("p1 = " + str(p1))
print ("o1.m1 = " + str(o1.m1))
o1.f2(p1)
o1.f2(p1)
p1 = o1.f2(p1)
print ("p1 = " + str(p1))
print ("o1.m1 = " + str(o1.m1))


def f3(a):
    return a+1, a+2

b = f3(1)
print ("ZZ: " + str(b))

#exit(0)

def foundInList(theList, toFind):
    for i in theList:
        if (i == toFind):
            return True
    return False

def mergeLists(a, b):
    merged = a
    for j in b:
        found = False
        for i in a:
            if i == j:
                found = True
        if not found:
            merge.append(j)
    return merged

class Dir:
    def __init__(self, parent):
        self.parent = parent
        self.name = ""
        self.fileSizes = []
        self.fileNames = []
        self.subDirs = []
        self.totalSize = 0

    def sizeRecur(self):
        size = 0
        for f in self.fileSizes:
            size = size + f
        for d in self.subDirs:
            size = size + d.sizeRecur()
        self.totalSize = size
        return size

    def print(self, curSpacing):
        print (curSpacing  + self.name + ": " + str(self.totalSize))
        curSpacing += "  "
        for d in self.subDirs:
            d.print(curSpacing)

    def dirsLargerOrEq(self, minSize, dirList):
        if (self.totalSize >= minSize):
            dirList.append(self.totalSize)
        for d in self.subDirs:
            result = d.dirsLargerOrEq(minSize, dirList)
            dirList = mergeLists(result, dirList)
        return dirList

    def totalSizeOfDirsLessThanMax(self, totalSizeOfDirsLessThanMax):

        mySize = 0
        for f in self.fileSizes:
            mySize = mySize + f
        for d in self.subDirs:
            subTotal = 0
            result = d.totalSizeOfDirsLessThanMax(subTotal)
            mySize += result[0]
            totalSizeOfDirsLessThanMax += result[1]
        self.totalSize = mySize
        print ("DIR: " + self.name + ", size=" + str(mySize) + ", Total = " + str(totalSizeOfDirsLessThanMax))
        if (mySize < maxDirSize):
            print ("ADDED")
            totalSizeOfDirsLessThanMax = totalSizeOfDirsLessThanMax + mySize
            print ("ADDED New: " + str(totalSizeOfDirsLessThanMax))
            #ggg = ggg + mySize

        return mySize, totalSizeOfDirsLessThanMax



f = open("dec7-dataset.txt", "rt")
lineCount = 0
root = Dir(None)
root.name = "."
curDir = root
#root.fileSizes = [1, 2, 3]
#subD1 = Dir()
#subD1.fileSizes = [2, 3]
#root.subDirs.append(subD1)


for line in f:
    line = line.strip()
    lineCount = lineCount + 1
    print ("")
    print ("Cur Dir = " + curDir.name)
    print(line)

    result = re.match("^\$\s+cd\s+(.+)$", line)
    if result:
        print ("cd to: " + result.group(1))
        if (result.group(1) == "/"):
            curDir = root
        elif (result.group(1) == ".."):
            curDir = curDir.parent
        else:
            found = False
            for d in curDir.subDirs:
                if (d.name == result.group(1)):
                    found = True
                    curDir = d
                    print ("Changing to " + d.name)
            if (not found):
                print ("Creating new dir " + result.group(1))
                newDir = Dir(curDir)
                newDir.name = result.group(1)
                curDir.subDirs.append(newDir)
                curDir = newDir
    result = re.match("^\$\sls\s*$", line)
    if result:
        print ("ls")
    result = re.match("^dir\s+(.+)$", line)
    if result:
        print ("SUB DIR:" + result.group(1))
    result = re.match("^(\d+)\s+(.+)$", line)
    if result:
        if (not foundInList(curDir.fileNames, result.group(2))):
            print ("FILE SIZE: " + result.group(1))
            curDir.fileSizes.append(int(result.group(1)))
            curDir.fileNames.append(result.group(2))

f.close()

totalSizeOfDirs = 0
root.totalSizeOfDirsLessThanMax(totalSizeOfDirs)
#root.print("")
fileSystemSize = root.totalSize
freeSpace = FSSizeTotal - fileSystemSize
spaceNeeded = freeSpaceNeeded - freeSpace
print ("File System Size: " + str(fileSystemSize))
print ("Free Space: " + str(freeSpace))
print ("Free Space needed: " + str(freeSpaceNeeded))
print ("Free Space to make: " + str(spaceNeeded))
dirList = root.dirsLargerOrEq(spaceNeeded, [])
dirList.sort()
print ("DIRS: " + str(dirList))

#print("Total of lines: " + str(lineCount))
#print("Total size of dirs with less than " + str(maxDirSize) + ": " + str(totalSizeOfDirs))
#print("Total size of dirs with less than " + str(maxDirSize) + ": " + str(g))
