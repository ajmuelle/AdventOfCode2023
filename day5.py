import numpy as np

with open("input/day5.txt") as day5:
    lines = day5.readlines()

seeds = [int(seed) for seed in lines[0].split(": ")[1].split()]

# make it easier to form patterns later
del lines[0:2]
lines.append("\n")

mapNames = ["seed-to-soil",
            "soil-to-fertilizer",
            "fertilizer-to-water",
            "water-to-light",
            "light-to-temperature",
            "temperature-to-humidity",
            "humidity-to-location"]
mapFunctions = [None] * 7
mapIndex = 0
currentTriples = []

def getMapFromTriples(triples):
    """Given a set of triples, return a function mapping x to y"""

    # making convenience copies partially to avoid overwriting triples
    sourceRangeStarts = [triple[1] for triple in triples]
    sourceRangeStops = [triple[1] + triple[2] for triple in triples]

    # the number you need to add to get from source to destination
    destRangeDeltas = [triple[0] - triple[1] for triple in triples]

    # define the function mapping x to y, encapsulating the above lists
    def tripleMap(x):
        for rangeIndex in range(len(sourceRangeStarts)):
            sourceRangeStart = sourceRangeStarts[rangeIndex]
            sourceRangeStop = sourceRangeStops[rangeIndex]
            destRangeDelta = destRangeDeltas[rangeIndex]

            # if x is in the correct range, apply the delta and return
            if sourceRangeStart <= x < sourceRangeStop:
                return x + destRangeDelta

        # base case: x wasn't in any range, so just return it unmodified
        return x

    return tripleMap

for line in lines:
    mapName = mapNames[mapIndex]

    # line is just a newline
    if len(line) == 1:
        mapFunctions[mapIndex] = getMapFromTriples(currentTriples)
        mapIndex += 1

    # line is the start of a new map
    elif mapName in line:
        currentTriples = []

    # line is part of the current map
    else:
        triple = [int(x) for x in line.split()]
        currentTriples.append(triple)

seedLocations = []

# apply the chain of map functions to get the seed -> location mapping
for seed in seeds:
    currentValue = seed
    for mapFunction in mapFunctions:
        currentValue = mapFunction(currentValue)
    seedLocations.append(currentValue)

print(np.min(seedLocations))
