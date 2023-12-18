import numpy as np

with open("input/day14tiny.txt") as day14:
    lines = day14.readlines()

numRows = len(lines)
numCols = len(lines[0][:-1])

# convert input to 2d array of chars
chars2d = []
for line in lines:
    chars2d.append(list(line.replace("\n", "")))

def findOpenRowNorth(row, col):
    while row > 0:
        if chars2d[row - 1][col] != ".":
            return row
        row -= 1
    return 0

def findOpenRowSouth(row, col):
    while row < numRows - 1:
        if chars2d[row + 1][col] != ".":
            return row
        row += 1
    return numRows - 1

def findOpenColWest(row, col):
    while col > 0:
        if chars2d[row][col - 1] != ".":
            return col
        col -= 1
    return 0

def findOpenColEast(row, col):
    while col < numCols - 1:
        if chars2d[row][col + 1] != ".":
            return col
        col += 1
    return numCols - 1

def rollNorth():
    # first row doesn't move
    for row in range(1, numRows):
        for col in range(numCols):
            if chars2d[row][col] == "O":
                newRow = findOpenRowNorth(row, col)
                if newRow != row:
                    chars2d[newRow][col] = "O"
                    chars2d[row][col] = "."

def rollSouth():
    # last row doesn't move
    for row in range(numRows - 2, -1, -1):
        for col in range(numCols):
            if chars2d[row][col] == "O":
                newRow = findOpenRowSouth(row, col)
                if newRow != row:
                    chars2d[newRow][col] = "O"
                    chars2d[row][col] = "."

def rollWest():
    for row in range(numRows):
        # first col doesn't move
        for col in range(1, numCols):
            if chars2d[row][col] == "O":
                newCol = findOpenColWest(row, col)
                if newCol != col:
                    chars2d[row][newCol] = "O"
                    chars2d[row][col] = "."

def rollEast():
    for row in range(numRows):
        # last col doesn't move
        for col in range(numCols - 2, -1, -1):
            if chars2d[row][col] == "O":
                newCol = findOpenColEast(row, col)
                if newCol != col:
                    chars2d[row][newCol] = "O"
                    chars2d[row][col] = "."

##### PART ONE #####
# rollNorth()

##### PART TWO #####
def spinCycle():
    rollNorth()
    rollWest()
    rollSouth()
    rollEast()

for x in range(1000000000):
    spinCycle()

# count Os in each row
counts = [np.sum([char == "O" for char in chars]) for chars in chars2d]

total = 0
for index, count in enumerate(counts):
    total += (numRows - index) * count

print(total)

pass