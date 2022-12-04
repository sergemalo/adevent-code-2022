import re


class SectionRange:
    def __init__(self, idx0, idx1):
        self.startIdx = idx0
        self.endIdx = idx1

    def contains(self, otherSR):
        if (self.startIdx <= otherSR.startIdx) and (self.endIdx >= otherSR.endIdx):
            return True
        return False


f = open("dec4-dataset.txt", "rt")
lineCount = 0
sectionRangeContained = 0
for line in f:
    line = line.strip()
    lineCount = lineCount + 1
    print(line)
    pattern = "^(\d+)-(\d+),(\d+)-(\d+)$"
    result = re.match(pattern, line)
    if result:
        sr1 = SectionRange(int(result.group(1)), int(result.group(2)))
        sr2 = SectionRange(int(result.group(3)), int(result.group(4)))
        if (sr1.contains(sr2) or (sr2.contains(sr1))):
            #print("Result: " + str(result.group(1)))
            #print("Result: " + str(result.group(2)))
            #print("Result: " + str(result.group(3)))
            #print("Result: " + str(result.group(4)))
            sectionRangeContained = sectionRangeContained + 1
            print("Total Section Ranged contained: " + str(sectionRangeContained))
    else:
        raise ("Unable to match pattern in line: " + line)


f.close()

print("Total of lines: " + str(lineCount))
print("Total Section Ranged contained: " + str(sectionRangeContained))
