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
        currentSearchArea.append(line)
searchAreas.append(currentSearchArea)

pass
