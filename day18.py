import numpy as np
# from skspatial.measurement import area_signed
import matplotlib; matplotlib.use("Qt5Agg"); import matplotlib.pyplot as plt; plt.ion()

with open("input/day18tiny.txt") as day18:
    lines = day18.readlines()

deltas = {"R": np.array([0, 1]),
          "U": np.array([-1, 0]),
          "L": np.array([0, -1]),
          "D": np.array([1, 0])}

def applyDelta(row, col, direction, steps):
    return tuple(np.array([row, col]) + deltas[direction] * steps)

directions = []
stepsArray = []
rgbArray = []
points = [(0, 0)]
minRow, maxRow, minCol, maxCol = 0, 0, 0, 0
row, col = 0, 0


for line in lines:
    direction, stepsStr, rgbParen = line.split(" ")

    steps = int(stepsStr)
    rgb = rgbParen[2:8]

    directions.append(direction)
    stepsArray.append(steps)
    rgbArray.append(rgb)

    row, col = applyDelta(row, col, direction, steps)
    points.append((row, col))

    # update extremes
    if row > maxRow:
        maxRow = row
    elif row < minRow:
        minRow = row
    if col > maxCol:
        maxCol = col
    elif col < minCol:
        minCol = col


# correct shape such that upper left corner of enclosing box is 0,0
rowDelta = 0 - minRow
colDelta = 0 - minCol
points = [applyDelta(row, col, "D", rowDelta) for row, col in points]
points = [applyDelta(row, col, "R", colDelta) for row, col in points]

# fix the maxes and mins to be relative to the new shape
minRow, minCol = 0, 0
maxRow, _ = applyDelta(maxRow, 0, "D", rowDelta)
_, maxCol = applyDelta(0, maxCol, "R", colDelta)

# fill in the lava
sharpsArray = np.zeros((maxRow, maxCol))
sharpSeen = points[0] == (0,0)
cornerDir = "D"
for row in range(maxRow):
    for col in range(maxCol):
        pass

# 46514 too low

pass
