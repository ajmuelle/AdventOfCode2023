import copy
import sys

import numpy as np

with open("input/day8.txt") as day8:
    lines = day8.readlines()

leftRightStr = lines[0][:-1]
leftRightLen = len(leftRightStr)
# convert left/right to indices
leftRightMap = {"L": 0, "R": 1}
leftRightList = [leftRightMap[letter] for letter in leftRightStr]

del lines[0:2]

### PART ONE VERSION ###
# letterTripleMap = {}
# for line in lines:
#     key, value = line.split(" = ")
#     values = value.replace("\n", "")[1:-1].split(", ")
#     letterTripleMap[key] = values
#
# currentValue = "AAA"
# count = 0
# while currentValue != "ZZZ":
#     currentDirection = leftRightList[count % len(leftRightList)]
#     currentValue = letterTripleMap[currentValue][currentDirection]
#     count += 1
#
# print(count)

### PART TWO VERSION ###

aIndices = []
zIndices = {}   # hashmap for speed of membership checking

tripleToIndex = {}
valuePairs = []
for index, line in enumerate(lines):
    key, value = line.split(" = ")

    if key[2] == "Z":
        zIndices[index] = 0
    elif key[2] == "A":
        aIndices.append(index)

    tripleToIndex[key] = index

    values = value.replace("\n", "")[1:-1].split(", ")
    valuePairs.append(values)

indexMap = {}
for index, valuePair in enumerate(valuePairs):
    valueLeft = tripleToIndex[valuePair[0]]
    valueRight = tripleToIndex[valuePair[1]]
    indexMap[index] = {"L": valueLeft, "R": valueRight}

indexPathMap = {}

def findZ(lineIndex, leftRightIndex):
    count = 0
    while lineIndex not in zIndices:
        count += 1
        try:
            nextDirection = leftRightStr[leftRightIndex]
        except IndexError:
            leftRightIndex = leftRightIndex % leftRightLen
            nextDirection = leftRightStr[leftRightIndex]
        lineIndex = indexMap[lineIndex][nextDirection]
        leftRightIndex += 1
    return count


# don't ask me why this works (I think it's an accident)
counts = [findZ(aIndex, 0) for aIndex in aIndices]
print(np.lcm.reduce(counts))


##### USELESS FUNCTION GRAVEYARD #####


def followPath(startIndex, path):
    if path in indexPathMap[startIndex]:
        return indexPathMap[startIndex][path]
    # TODO: potentially store subsets of path?
    currentIndex = startIndex
    for direction in path:
        currentIndex = indexMap[currentIndex][direction]
    indexPathMap[currentIndex] = path
    return currentIndex

def getNextNTurns(currentIndex, N):
    newIndex = currentIndex + N
    if newIndex <= leftRightLen:
        # base case, no overflow
        return newIndex, leftRightStr[currentIndex:newIndex]

    # get rest of string before overflow
    indexDiff = leftRightLen - currentIndex
    currentStr = leftRightStr[currentIndex:]
    newIndex -= indexDiff

    # iterate until no overflow
    while(newIndex > leftRightLen):
        currentStr += leftRightStr
        newIndex -= leftRightLen

    # add the final piece and return
    currentStr += leftRightStr[:newIndex]
    return newIndex, currentStr
