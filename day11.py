import numpy as np

with open("input/day11.txt") as day11:
    lines = day11.readlines()

lineLength = len(lines[0]) - 1  # ignore the newline

# expand space vertically
dotsLine = "".join(["."] * lineLength) + "\n"
dotLineIndices = []
for index, line in enumerate(lines):
    if line == dotsLine:
        dotLineIndices.append(index)
for index in reversed(dotLineIndices):
    lines.insert(index, dotsLine)

# expand space horizontally
columnsWithGalaxies = set()
for line in lines:
    for index, char in enumerate(line):
        if char == "#":
            columnsWithGalaxies.add(index)
allColumnIndices = set(range(lineLength))
emptyColumns = allColumnIndices.difference(columnsWithGalaxies)
for column in reversed(list(emptyColumns)):
    for line in lines:
        line = f"{line[:column]}.{line[column:]}"

# compute galactic indices
galaxyCoords = []
for lineIndex, line in enumerate(lines):
    for charIndex, char in enumerate(line):
        if char == "#":
            galaxyCoords.append((lineIndex, charIndex))

pass
