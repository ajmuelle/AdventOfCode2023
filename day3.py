import numpy as np

with open("input/day3.txt") as day3:
    lines = day3.readlines()

##### PART ONE SOLUTION #####

def isPart(numberStr, rowIndex, colIndex):
    # index error = literal edge case
    for lineIndex in range(rowIndex - 1, rowIndex + 2):
        if lineIndex == -1:
            continue
        elif lineIndex == len(lines):
            break
        line = lines[lineIndex]
        for charIndex in range(colIndex - 1, colIndex + len(numberStr) + 1):
            if charIndex == -1:
                continue
            elif charIndex == len(line):
                break
            char = line[charIndex]
            if char != "." and char != "\n" and not char.isdigit():
                return True
    return False

# numbers = []
# currentStr = ""
#
# for rowIndex, line in enumerate(lines):
#     for colIndex, char in enumerate(line):
#         if char.isdigit():
#             currentStr += char
#         elif currentStr:
#             # we have reached a non-number char with a number to its left
#             if isPart(currentStr, rowIndex, colIndex - len(currentStr)):
#                 numbers.append(int(currentStr))
#             else:
#                 print(f"{currentStr} is not a part #")
#             currentStr = ""

# print(np.sum(numbers))
# 353712 too low
# 420314 too low
# 536523 too high

##### PART TWO SOLUTION #####

gears = []

def lookLeft(line, colIndex) -> str:
    leftIndex = 1
    leftStr = ""
    while colIndex - leftIndex >= 0 and line[colIndex - leftIndex].isdigit():
        leftStr = line[colIndex - leftIndex] + leftStr
        leftIndex += 1
    return leftStr

def lookRight(line, colIndex) -> str:
    rightIndex = 1
    rightStr = ""
    while colIndex + rightIndex < len(line) and line[colIndex + rightIndex].isdigit():
        rightStr = rightStr + line[colIndex + rightIndex]
        rightIndex += 1
    return rightStr

def lookBoth(line, colIndex) -> list:
    left, middle, right = "", "", ""
    if colIndex > 0 and line[colIndex - 1].isdigit():
        left = lookLeft(line, colIndex)
    if line[colIndex].isdigit():
        middle = line[colIndex]
    if colIndex < len(line) - 1 and line[colIndex + 1].isdigit():
        right = lookRight(line, colIndex)

    all3 = left + middle + right

    if not all3:
        return []

    if left and right and not middle:
        return [int(left), int(right)]

    return [int(all3)]

def getAdjacentNumbers(rowIndex, colIndex) -> list:
    firstRow = rowIndex == 0
    firstCol = colIndex == 0
    lastRow = rowIndex == len(lines) - 1
    lastCol = colIndex == len(lines[rowIndex]) - 1
    adjNumbers = []
    # left
    if not firstCol and lines[rowIndex][colIndex - 1].isdigit():
        leftStr = lookLeft(lines[rowIndex], colIndex)
        adjNumbers.append(int(leftStr))
    # right
    if not lastCol and lines[rowIndex][colIndex + 1].isdigit():
        rightStr = lookRight(lines[rowIndex], colIndex)
        adjNumbers.append(int(rightStr))
    # top
    if not firstRow:
        adjNumbers += lookBoth(lines[rowIndex - 1], colIndex)
    # bottom
    if not lastRow:
        adjNumbers += lookBoth(lines[rowIndex + 1], colIndex)
    return adjNumbers

for rowIndex, line in enumerate(lines):
    for charIndex, char in enumerate(line):
        if char == "*":
            adjNumbers = getAdjacentNumbers(rowIndex, charIndex)
            if len(adjNumbers) == 2:
                gears.append(adjNumbers[0] * adjNumbers[1])

print(np.sum(gears))
