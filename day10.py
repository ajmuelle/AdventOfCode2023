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

pathCoords = {index: [] for index in range(len(lines))}

def followPath(current, destination, direction, count):
    while current != destination or count == 0:
        pathCoords[current[0]].append(current[1])
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

# part 1
# print(count // 2)

# part 2
pathCoords = {index: np.sort(coords) for index, coords in pathCoords.items() if len(coords) > 0}

# run this only once to make a version of day 10 input that I can actually see
# newLines = []
# for lineIndex, line in enumerate(lines):
#     newLine = ""
#     for charIndex, char in enumerate(line):
#         if lineIndex in pathCoords and charIndex in pathCoords[lineIndex]:
#             newLine += char
#         else:
#             newLine += "."
#     newLine += "\n"
#     newLines.append(newLine)
# with open("input/day10fake.txt", "w") as day10fake:
#     day10fake.writelines(newLines)

def isCharEnclosed(lineIndex, charIndex, pipeIndices):
    barCount = 0
    line = lines[lineIndex]
    FSeen = False
    LSeen = False
    for rightIndex in range(charIndex + 1, len(line)):
        if rightIndex in pipeIndices:
            currentChar = line[rightIndex]
            if currentChar == "|":
                barCount += 1
            elif (FSeen and currentChar == "J") or (LSeen and currentChar == "7"):
                barCount += 1
                FSeen = False
                LSeen = False
            elif FSeen and currentChar == "7":
                FSeen = False
            elif LSeen and currentChar == "J":
                LSeen = False
            elif currentChar == "F":
                FSeen = True
            elif currentChar == "L":
                LSeen = True

    return barCount % 2 == 1


count = 0
for lineIndex, pipeIndices in pathCoords.items():
    charsEnclosed = []
    for charIndex in range(pipeIndices[0], pipeIndices[-1] + 1):
        currentChar = lines[lineIndex][charIndex]
        if charIndex not in pipeIndices:
            if isCharEnclosed(lineIndex, charIndex, pipeIndices):
                count += 1
                charsEnclosed.append(charIndex)
    print(f"on line {lineIndex} the enclosed chars are {charsEnclosed}")

print(count)

