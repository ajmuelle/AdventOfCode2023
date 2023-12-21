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
        currentSearchArea.append(list(line.replace("\n","")))
searchAreas.append(currentSearchArea)


class SmudgeException(Exception):
    def __init__(self, row, col):
        self.row = row
        self.col = col

def rowDiff(searchArea, row1, row2):
    diff = 0
    smudgeIndex = 0
    for index in range(len(searchArea[0])):
        if searchArea[row1][index] != searchArea[row2][index]:
            diff += 1
            smudgeIndex = index
    if diff == 1:
        raise SmudgeException(row1, smudgeIndex)
    return diff

def colDiff(searchArea, col1, col2):
    diff = 0
    smudgeIndex = 0
    for index in range(len(searchArea)):
        if searchArea[index][col1] != searchArea[index][col2]:
            diff += 1
            smudgeIndex = index
    if diff == 1:
        raise SmudgeException(smudgeIndex, col1)
    return diff

def columnsMatch(searchArea, column1, column2):
    return colDiff(searchArea, column1, column2) == 0

def rowsMatch(searchArea, row1, row2):
    return rowDiff(searchArea, row1, row2) == 0

def verifyColumnReflection(searchArea, column):
    lineLength = len(searchArea[0])
    left = column
    right = column + 1
    numSmudges = 0
    while left >= 0 and right < lineLength:
        try:
            if not columnsMatch(searchArea, left, right):
                return False
        except SmudgeException as e:
            numSmudges += 1
            searchArea[e.row][e.col] = "O"
            print(f"smudge found at row {e.row}, column {e.col}:")
            for line in searchArea:
                print("".join(line))
        left -= 1
        right += 1
    return numSmudges == 1

def verifyRowReflection(searchArea, row):
    numRows = len(searchArea)
    top = row
    bottom = row + 1
    numSmudges = 0
    while top >= 0 and bottom < numRows:
        try:
            if not rowsMatch(searchArea, top, bottom):
                return False
        except SmudgeException as e:
            numSmudges += 1
            searchArea[e.row][e.col] = "O"
            print(f"smudge found at row {e.row}, column {e.col}")
            for line in searchArea:
                print("".join(line))
        top -= 1
        bottom += 1
    return numSmudges == 1

horizontalMirrors = []
verticalMirrors = []

for searchArea in searchAreas:
    print("-----NEW SEARCH AREA-----")
    for index in range(len(searchArea) - 1):
        if verifyRowReflection(searchArea, index):
            horizontalMirrors.append(index + 1)
            print(f"{index + 1} added to horizontal mirrors")
            break
    else:
        for index in range(len(searchArea[0]) - 1):
            if verifyColumnReflection(searchArea, index):
                verticalMirrors.append(index + 1)
                print(f"{index + 1} added to vertical mirrors")
                break

print(np.sum(verticalMirrors) + 100 * np.sum(horizontalMirrors))
# 26755 too low
# 31485 too low

# part 2
# 9973 too low
# 28518 too low
# 34607 too high
