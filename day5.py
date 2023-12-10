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

def getMapFromTriples(triples, sign=1):
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
                return x + destRangeDelta * sign

        # base case: x wasn't in any range, so just return it unmodified
        return x

    return tripleMap

locationMax = 0

for line in lines:
    mapName = mapNames[mapIndex]

    # line is just a newline
    if len(line) == 1:
        mapFunctions[mapIndex] = getMapFromTriples(currentTriples, 1)
        mapIndex += 1
        # for part 2
        # if "location" in mapName:
        #     for triple in currentTriples:
        #         tripleRangeMax = triple[0] + triple[2]
        #         if tripleRangeMax > locationMax:
        #             locationMax = tripleRangeMax

    # line is the start of a new map
    elif mapName in line:
        currentTriples = []

    # line is part of the current map
    else:
        triple = [int(x) for x in line.split()]
        currentTriples.append(triple)

def applyFunctionChain(x, chain):
    """Apply the chain of map functions to get the seed -> location mapping"""
    for mapFunction in chain:
        x = mapFunction(x)
        # print(x)
    return x

### PART ONE VERSION ###

seedLocations = []
# for seed in seeds:
#     seedLocation = applyFunctionChain(seed, mapFunctions)
#     seedLocations.append(seedLocation)
#
# print(np.min(seedLocations))

### PART TWO VERSION ###

# BAD CODE, TAKES FOREVER TO RUN
minLocation = np.inf
numSeeds = len(seeds) // 2
for index, value in enumerate(seeds):
    if index % 2 == 0:
        rangeStart = int(value)
    else:
        print(f"now processing seed {index // 2} of {numSeeds}")
        for seed in range(rangeStart, rangeStart + value):
            seedLocation = applyFunctionChain(seed, mapFunctions)
            if seedLocation < minLocation:
                minLocation = seedLocation

print(minLocation)

# BAD CODE, OUTPUTS WRONG ANSWER
# print(f"locationMax = {locationMax}")
# for location in range(locationMax):
#     seed = applyFunctionChain(location, mapFunctions[::-1])
#     for index, value in enumerate(seeds):
#         if index % 2 == 0:
#             rangeStart = int(value)
#             # print(f"range start = {rangeStart}")
#         else:
#             if rangeStart <= seed < rangeStart + int(value):
#                 minLocation = location
#                 break
#
# print(minLocation)
