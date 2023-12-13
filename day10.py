import numpy as np

with open("input/day10.txt") as day10:
    lines = day10.readlines()

def getSLocation():
    for lineIndex, line in enumerate(lines):
        for charIndex, char in enumerate(line):
            if char == "S":
                return (lineIndex, charIndex)

SLocation = getSLocation()

validNextTiles = {
    "north": {"7": "west", "|": "north", "F": "east", "S": None},
    "east": {"J": "north", "-": "east", "7": "south", "S": None},
    "south": {"L": "east", "|": "south", "J": "west", "S": None},
    "west": {"F": "south", "-": "west", "L": "north", "S": None}
}

# (line, column)
directionDeltas = {
    "north": (-1, 0),
    "east": (0, 1),
    "south": (1, 0),
    "west": (0, -1)
}

def applyDelta(coord, direction):
    delta = directionDeltas[direction]
    return (coord[0] + delta[0],
            coord[1] + delta[1])

def getSurroundings(coord):
    surroundings = {}
    for direction in ["north", "east", "south", "west"]:
        try:
            x, y = applyDelta(coord, direction)
            surroundings[direction] = lines[x][y]
        except IndexError:
            continue
    return surroundings

def followPath(current, destination, direction, count):
    while current != destination or count == 0:
        surroundings = getSurroundings(current)
        nextTile = surroundings[direction]
        current = applyDelta(current, direction)
        count += 1
        direction = validNextTiles[direction][nextTile]
    return count
    # return followPath(current, destination, direction, count)

surroundings = getSurroundings(SLocation)

# cheating a bit, we know the tile north of S is valid
count = followPath(SLocation, SLocation, "north", 0)

print(count // 2)
