import numpy as np

with open("input/day17.txt") as day17:
    lines = day17.readlines()

numRows = len(lines)
numCols = len(lines[0][:-1])

# lost of code modified slightly from day 10
directionDeltas = {
    "north": (-1, 0),
    "east": (0, 1),
    "south": (1, 0),
    "west": (0, -1)
}

def applyDelta(row, col, direction):
    delta = directionDeltas[direction]
    return (row + delta[0],
            col + delta[1])

def getSurroundings(row, col):
    surroundings = {}
    for direction in ["north", "east", "south", "west"]:
        try:
            x, y = applyDelta(row, col, direction)
            surroundings[direction] = lines[x][y]
        except IndexError:
            continue
    return surroundings

row, col = 0, 0
consecutive = 0
last = ""

backwardsMap = {"north": "south",
                "east": "west",
                "south": "north",
                "west": "east"}

while row < numRows - 1 or col < numCols - 1:
    surroundings = getSurroundings(row, col)
    # remove edge cases
    if row == 0:
        surroundings.pop("north", None)
    elif row == numRows - 1:
        surroundings.pop("south", None)
    if col == 0:
        surroundings.pop("west", None)
    elif col == numCols - 1:
        surroundings.pop("east", None)
    # can't go backwards
    if last in backwardsMap:
        surroundings.pop(backwardsMap[last], None)
    # after 3 must turn
    if consecutive == 3:
        surroundings.pop(last, None)
