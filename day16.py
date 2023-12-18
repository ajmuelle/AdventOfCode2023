import copy

import numpy as np

with open("input/day16.txt") as day16:
    lines = day16.readlines()

# next 11 lines copy-pasted from day 14
numRows = len(lines)
numCols = len(lines[0][:-1])

# convert input to 2d array of chars
chars2d = []
for line in lines:
    chars2d.append(list(line.replace("\n", "")))

# convenience function for debugging
def stringify(map):
    return "\n".join(["".join(chars) for chars in map])


def moveOneSpace(direction, row, col):
    match direction:
        case ">":   # right
            return row, col + 1
        case "v":   # down
            return row + 1, col
        case "<":   # left
            return row, col - 1
        case "^":   # up
            return row - 1, col
        case _:
            raise KeyError

def validSpace(row, col):
    return 0 <= row < numRows and 0 <= col < numCols

mirrorMap = {"\\": {">": "v",
                    "v": ">",
                    "<": "^",
                    "^": "<"},
             "/": {">": "^",
                   "v": "<",
                   "<": "v",
                   "^": ">"}}

splitterMap = {"|": {">": "^v",
                     "v": "v",
                     "<": "^v",
                     "^": "^"},
               "-": {">": ">",
                     "v": "<>",
                     "<": "<",
                     "^": "<>"}}

initialMap = copy.deepcopy(chars2d)
energizedMap = copy.deepcopy(initialMap)

def followBeamPath(direction, row, col):
    while validSpace(row, col) and chars2d[row][col] != direction:
        energizedMap[row][col] = "#"
        if chars2d[row][col] == ".":
            chars2d[row][col] = direction
        if not validSpace(row, col):
            return
        if chars2d[row][col] in mirrorMap:
            direction = mirrorMap[chars2d[row][col]][direction]
            # row, col = moveOneSpace(direction, row, col)
        elif chars2d[row][col] in splitterMap:
            direction = splitterMap[chars2d[row][col]][direction]
            if len(direction) == 2:
                dir1, dir2 = tuple(direction)
                # row1, col1 = moveOneSpace(dir1, row, col)
                # row2, col2 = moveOneSpace(dir2, row, col)
                # recursion is dangerous
                followBeamPath(dir1, row, col)
                followBeamPath(dir2, row, col)
                return
            else:
                # row, col = moveOneSpace(direction, row, col)
                pass
        row, col = moveOneSpace(direction, row, col)

##### PART ONE #####
# followBeamPath(">", 0, 0)
#
# print(np.sum([np.sum([char == "#" for char in chars]) for chars in energizedMap]))

##### PART TWO #####
energizedSums = []

for topCol in range(numCols):
    print(f"iteration {topCol} of loop 1")
    energizedMap = copy.deepcopy(initialMap)
    chars2d = copy.deepcopy(initialMap)
    followBeamPath("v", 0, topCol)
    energizedSum = np.sum([np.sum([char == "#" for char in chars]) for chars in energizedMap])
    energizedSums.append(energizedSum)

for bottomCol in range(numCols):
    print(f"iteration {bottomCol} of loop 2")
    energizedMap = copy.deepcopy(initialMap)
    chars2d = copy.deepcopy(initialMap)
    followBeamPath("^", numRows - 1, bottomCol)
    energizedSum = np.sum([np.sum([char == "#" for char in chars]) for chars in energizedMap])
    energizedSums.append(energizedSum)

for leftRow in range(numRows):
    print(f"iteration {leftRow} of loop 3")
    energizedMap = copy.deepcopy(initialMap)
    chars2d = copy.deepcopy(initialMap)
    followBeamPath(">", leftRow, 0)
    energizedSum = np.sum([np.sum([char == "#" for char in chars]) for chars in energizedMap])
    energizedSums.append(energizedSum)

for rightRow in range(numRows):
    print(f"iteration {rightRow} of loop 4")
    energizedMap = copy.deepcopy(initialMap)
    chars2d = copy.deepcopy(initialMap)
    followBeamPath("<", rightRow, numCols - 1)
    energizedSum = np.sum([np.sum([char == "#" for char in chars]) for chars in energizedMap])
    energizedSums.append(energizedSum)
# followBeamPath("v", 0, 3)
# pass
print(np.max(energizedSums))
