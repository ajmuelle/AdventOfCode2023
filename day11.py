import numpy as np

with open("input/day11.txt") as day11:
    lines = day11.readlines()

lineLength = len(lines[0]) - 1  # ignore the newline

# find empty lines
dotsLine = "".join(["."] * lineLength) + "\n"
emptyLines = []
for index, line in enumerate(lines):
    if line == dotsLine:
        emptyLines.append(index)

# find empty columns
columnsWithGalaxies = set()
for line in lines:
    for index, char in enumerate(line):
        if char == "#":
            columnsWithGalaxies.add(index)
allColumnIndices = set(range(lineLength))
emptyColumns = sorted(allColumnIndices.difference(columnsWithGalaxies))

# compute (pre-expansion) galactic indices
galaxyCoords = []
for lineIndex, line in enumerate(lines):
    for charIndex, char in enumerate(line):
        if char == "#":
            galaxyCoords.append((lineIndex, charIndex))

def distExpanded(coord1, coord2):
    """Account for universe expansion without actually computing it."""
    # using x to mean row/line, y to mean column
    bigX, smallX = (coord1[0], coord2[0]) if coord1[0] > coord2[0] else (coord2[0], coord1[0])
    bigY, smallY = (coord1[1], coord2[1]) if coord1[1] > coord2[1] else (coord2[1], coord1[1])
    xDelta = bigX - smallX
    yDelta = bigY - smallY
    for x in range(smallX, bigX):
        if x in emptyLines:
            xDelta += 999999    # 1 in part 1
    for y in range(smallY, bigY):
        if y in emptyColumns:
            yDelta += 999999    # 1 in part 1
    return xDelta + yDelta

# compute minimum distances
minDists = []
for index1, coord1 in enumerate(galaxyCoords):
    for index2, coord2 in enumerate(galaxyCoords[index1:]):
        minDists.append(distExpanded(coord1, coord2))

print(np.sum(minDists))
