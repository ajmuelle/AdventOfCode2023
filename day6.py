import numpy as np

with open("input/day6.txt") as day6:
    lines = day6.readlines()

# part one version
# times = [int(x) for x in lines[0].split(":")[1].split()]
# distances = [int(x) for x in lines[1].split(":")[1].split()]

# part two version
times = [int(lines[0].split(":")[1].replace(" ", ""))]
distances = [int(lines[1].split(":")[1].replace(" ", ""))]

winCounts = []

for time, distance in zip(times, distances):
    winCount = 0
    for milliseconds in range(1, time):
        if (time - milliseconds) * milliseconds > distance:
            winCount += 1
    winCounts.append(winCount)

print(np.prod(winCounts))
