import numpy as np

with open("input/day13.txt") as day13:
    lines = day13.readlines()

searchAreas = []
currentSearchArea = []
for line in lines:
    if line == "\n":
        searchAreas.append(currentSearchArea)
        currentSearchArea = []
    else:
        currentSearchArea.append(line.replace("\n",""))
searchAreas.append(currentSearchArea)

pass

def columnsMatch(searchArea, column1, column2):
    for line in searchArea:
        if line[column1] != line[column2]:
            return False
    return True

def rowsMatch(searchArea, row1, row2):
    return searchArea[row1] == searchArea[row2]

def verifyColumnReflection(searchArea, column):
    lineLength = len(searchArea[0])
    left = column
    right = column + 1
    while left >= 0 and right < lineLength:
        if not columnsMatch(searchArea, left, right):
            return False
        left -= 1
        right += 1
    return True

def verifyRowReflection(searchArea, row):
    numRows = len(searchArea)
    top = row
    bottom = row + 1
    while top >= 0 and bottom < numRows:
        if not rowsMatch(searchArea, top, bottom):
            return False
        top -= 1
        bottom += 1
    return True

horizontalMirrors = []
verticalMirrors = []

for searchArea in searchAreas:
    for index in range(len(searchArea) - 1):
        if verifyRowReflection(searchArea, index):
            horizontalMirrors.append(index + 1)
    for index in range(len(searchArea[0]) - 1):
        if verifyColumnReflection(searchArea, index):
            verticalMirrors.append(index + 1)

print(np.sum(verticalMirrors) + 100 * np.sum(horizontalMirrors))
# 26755 too low
# 31485 too low
