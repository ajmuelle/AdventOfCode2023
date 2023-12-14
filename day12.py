import numpy as np

with open("input/day12.txt") as day12:
    lines = day12.readlines()

class SharpRun:
    def __init__(self, start, length):
        self.start = start
        self.length = length

    def __contains__(self, index):
        return self.start <= index < self.start + self.length


class Record:
    def __init__(self, line):
        self.symbols, countStr = line.split(" ")
        self.counts = countStr.rstrip("\n").split(",")

    def findSharpRuns(self):
        """ Determine where there are runs of sharps within the line. """
        self.sharpRuns = []
        sharpLength = 0
        for index, char in enumerate(self.symbols):
            if char == "#":
                sharpLength += 1
            elif sharpLength > 0:
                # if we got here, the last sharpLength chars were a sharp run
                sharpRun = SharpRun(index - sharpLength, sharpLength)
                self.sharpRuns.append(sharpRun)
                sharpLength = 0

    def permuteCounts(self):
        """ For each count, determine maximal set of start indices. """
        self.startIndices2d = []
        for index, count in enumerate(self.counts):
            leftIndex = self.leftBound(index)
            rightIndex = self.rightBound(index)
            maximalCount = (rightIndex - leftIndex) + 1 - count + 1
            sharpRuns = self.boundSharpRuns(leftIndex, rightIndex)
            for sharpRun in sharpRuns:
                if sharpRun.length > count:
                    if sharpRun.start < leftIndex:
                        maximalCount -= (sharpRun.length - (sharpRun.start + sharpRun.length - leftIndex))
                    else:
                        maximalCount -= (sharpRun.start + sharpRun.length - rightIndex)
                elif sharpRun.length < count:
                    pass
                else:   # exactly equal
                    pass

    def leftBound(self, index):
        """ Return the leftmost column that's valid for self.counts[index] """
        minIndex = 0
        for leftCountIndex in range(index):
            minIndex += (self.counts[leftCountIndex] + 1)
        return minIndex

    def rightBound(self, index):
        """ Return the rightmost column that's valid for self.counts[index] """
        maxIndex = len(self.symbols) - 1
        for rightCountIndex in range(len(self.symbols) - 1, index, -1):
            maxIndex -= (self.counts[rightCountIndex] + 1)
        return maxIndex

    def boundSharpRuns(self, left, right):
        """ Return the sharp runs that overlap the range [left, right] """
        overlappingRuns = []
        for sharpRun in self.sharpRuns:
            if (sharpRun.start <= right and
                sharpRun.start + sharpRun.length > left):
                overlappingRuns.append(sharpRun)
        return overlappingRuns


records = []
for line in lines:
    # using ugly, stateful OOP for purely aesthetic reasons
    record = Record(line)
    record.findSharpRuns()
    record.permuteCounts()
    records.append(record)
