import copy
import sys

import numpy as np

with open("input/day8.txt") as day8:
    lines = day8.readlines()

# convert left/right to indices
leftRightMap = {"L": 0, "R": 1}
leftRightList = [leftRightMap[letter] for letter in lines[0][:-1]]

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
    valueIndex0 = tripleToIndex[valuePair[0]]
    valueIndex1 = tripleToIndex[valuePair[1]]
    indexMap[index] = [valueIndex0, valueIndex1]

def notZ(indices):
    return indices[0] not in zIndices \
        # or indices[1] not in zIndices \
        # or indices[2] not in zIndices \
        # or indices[3] not in zIndices \
        # or indices[4] not in zIndices \
        # or indices[5] not in zIndices

currentIndices = aIndices[2:3]
count = 0
leftRightLen = len(leftRightList)
while notZ(currentIndices):
    currentDirection = leftRightList[count % leftRightLen]
    currentIndices = [indexMap[value][currentDirection] for value in currentIndices]
    count += 1

print(count)
