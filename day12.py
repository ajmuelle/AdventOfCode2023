import itertools

import numpy as np
import scipy.special

with open("input/day12tiny.txt") as day12:
    lines = day12.readlines()


def unfold(sharpPart, numberPart):
    newSharpPart = "?".join([sharpPart for x in range(5)])
    newNumberPart = ",".join([numberPart for x in range(5)])
    return newSharpPart, newNumberPart


def isValid(lineStr, numbers):
    sharpRuns = list(filter(None, lineStr.split(".")))
    if len(sharpRuns) != len(numbers):
        return False
    for index, run in enumerate(sharpRuns):
        if len(run) != numbers[index]:
            return False
    return True


def countArrangements(sharpPart, numbers):
    dots, sharps, qMarks = [], [], set()
    for index, char in enumerate(sharpPart):
        match char:
            case "#":
                sharps.append(index)
            case "?":
                qMarks.add(index)
            case _:
                dots.append(index)
    correctSharpCount = np.sum(numbers)
    visibleSharpCount = len(sharps)
    missingSharpCount = correctSharpCount - visibleSharpCount
    arrangementsUpperBound = scipy.special.comb(len(qMarks), missingSharpCount, exact=True)
    arrangements = 0

    # the set of all possible indices where a question mark is actually a sharp
    missingSharpCombs = itertools.combinations(qMarks, missingSharpCount)
    for comb in missingSharpCombs:
        sharpIndices = set(comb)
        dotIndices = qMarks.difference(sharpIndices)
        lineArray = np.array(list(sharpPart))
        lineArray[list(sharpIndices)] = "#"
        lineArray[list(dotIndices)] = "."
        lineStr = "".join(lineArray)
        if isValid(lineStr, numbers):
            arrangements += 1
            # print(lineStr)

    return arrangements


# part 2 idea: construct list containing folded count followed by 4 instances
# of what the count would be if you add a ? to the left, except when you know
# for sure that folded ends with # (in day12tiny this works on the first 5
# test cases but not the 6th, but 10 * 15 * 15 * 15 * 15 gets that answer)


permCounts = []
for line in lines:
    sharpPart, numberPart = line.replace("\n", "").split(" ")
    sharpPart, numberPart = unfold(sharpPart, numberPart)   # part 2 only
    numbers = [int(number) for number in numberPart.split(",")]

    permCount = countArrangements(sharpPart, numberPart)
    permCounts.append(permCount)

    pass

# the answer is undoubtedly less than 727925
print(np.sum(permCounts))
