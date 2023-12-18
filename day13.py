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

def rowDiff(searchArea, row1, row2):
    diff = 0
    for index in range(len(searchArea[0])):
        if searchArea[row1][index] != searchArea[row2][index]:
            diff += 1
    return diff

def colDiff(searchArea, col1, col2):
    diff = 0
    for index in range(len(searchArea)):
        if searchArea[index][col1] != searchArea[index][col2]:
            diff += 1
    return diff

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
    smudge = False
    while left >= 0 and right < lineLength:
        if not columnsMatch(searchArea, left, right):
            if colDiff(searchArea, left, right) == 1 and not smudge:
                smudge = True
            else:
                return False
        left -= 1
        right += 1
    return True

def verifyRowReflection(searchArea, row):
    numRows = len(searchArea)
    top = row
    bottom = row + 1
    smudge = False
    while top >= 0 and bottom < numRows:
        if not rowsMatch(searchArea, top, bottom):
            if rowDiff(searchArea, top, bottom) == 1 and not smudge:
                smudge = True
            else:
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
            break
    else:
        for index in range(len(searchArea[0]) - 1):
            if verifyColumnReflection(searchArea, index):
                verticalMirrors.append(index + 1)
                break

print(np.sum(verticalMirrors) + 100 * np.sum(horizontalMirrors))
# 26755 too low
# 31485 too low

# part 2
# 9973 too low
# 34607 too high
