import numpy as np
from scipy.special import comb

with open("input/day12.txt") as day12:
    lines = day12.readlines()

def partitionNumbers(segmentLengths, numbers):
    # TODO: handle base cases
    pass

permCounts = []
for line in lines:
    sharpPart, numberPart = line.replace("\n", "").split(" ")
    numbers = [int(number) for number in numberPart.split(",")]
    dots, sharps, qMarks = [], [], []
    for index, char in enumerate(sharpPart):
        match char:
            case "#":
                sharps.append(index)
            case "?":
                qMarks.append(index)
            case _:
                dots.append(index)
    correctSharpCount = np.sum(numbers)
    visibleSharpCount = len(sharps)
    missingSharpCount = correctSharpCount - visibleSharpCount
    permCountUpperBound = comb(len(qMarks), missingSharpCount, exact=True)

    permCount = 1
    segments = list(filter(lambda x: len(x) > 0, sharpPart.split(".")))
    segmentLengths = [len(segment) for segment in segments]
    partitions = partitionNumbers(segmentLengths, numbers)

    pass

print(np.sum(permCounts))
