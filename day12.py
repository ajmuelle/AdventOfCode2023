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


def hash(N, numbers, count):
    return f"{N};{str(numbers)};{count}"


comboCache = {}


def consecutiveCombos(N, numbers, count=0):
    global comboCache
    inputHash = hash(N, numbers, count)
    if inputHash in comboCache:
        return comboCache[inputHash]
    m = numbers[0]
    nn = len(numbers)
    if nn == 1:
        combos = [tuple(range(count+a, count+a+m)) for a in range(N - m + 1)]
    else:
        combos = []
        for x in range(N - m - 1, np.sum(numbers[1:]) + nn - 3, -1):
            leftCombo = tuple(range(count, count + m))
            rightCombos = consecutiveCombos(x, numbers[1:], count=(count + m + 1))
            combos += [leftCombo + rightCombo for rightCombo in rightCombos]
            count += 1
    comboCache[inputHash] = combos
    return combos


def consecutiveCombos_iterative(N, numbers):
    combosByNumber = []
    numnums = len(numbers)
    leftBound = 0
    for index, number in enumerate(numbers):
        leftSum = sum(numbers[:index + 1]) + index
        rightSum = sum(numbers[index + 1:]) if index + 1 < numnums else 0
        numCommas = numnums - (index + 1)
        rightBound = N - leftSum - rightSum - numCommas + 1
        combo = [tuple(range(leftBound + offset, leftBound + offset + number))
                 for offset in range(rightBound)]
        combosByNumber.append(combo)
        leftBound += (number + 1)
    pass
    # TODO: not this
    return tuple(itertools.chain.from_iterable(itertools.chain.from_iterable(combosByNumber)))


def processIndicator(indicator):
    if np.all(indicator):
        return "#"
    elif np.all(np.logical_not(indicator)):
        return "."
    else:
        return "?"


def sharpify(N, indices):
    lineArray = np.array(["." for x in range(N)])
    lineArray[list(indices)] = "#"
    return "".join(lineArray)


def countArrangements(sharpPart, numbers):
    dots, sharps, qMarks = [], set(), set()
    for index, char in enumerate(sharpPart):
        match char:
            case "#":
                sharps.add(index)
            case "?":
                qMarks.add(index)
            case _:
                pass
                # dots.append(index)
    correctSharpCount = np.sum(numbers)
    visibleSharpCount = len(sharps)
    missingSharpCount = correctSharpCount - visibleSharpCount

    # the set of all possible sharp indices that satisfy numbers, ignoring ?s
    # consecutiveSet = set(tuple(combo) for combo in consecutiveCombos(len(sharpPart), numbers))
    consecutiveSet = set(consecutiveCombos_iterative(len(sharpPart), numbers))
    arrangements = 0

    # the set of all possible indices where a question mark could be a sharp
    missingSharpCombs = itertools.combinations(qMarks, missingSharpCount)

    # add the known sharp indices to each element of the above set
    sharpPossibilitiesSet = set([tuple(sorted(sharps.union(comb))) for comb in missingSharpCombs])

    # don't bother searching if it's not in both sets
    searchSpaceSet = consecutiveSet.intersection(sharpPossibilitiesSet)
    print(f"the search space has {len(searchSpaceSet)} sets in it")

    # sharpStartIndicator = []    # whether each correct combo starts with sharp
    # sharpEndIndicator = []      # whether each correct combo ends in a sharp
    for comb in searchSpaceSet:
        sharpIndices = list(comb)
        lineStr = sharpify(len(sharpPart), sharpIndices)
        if isValid(lineStr, numbers):
            arrangements += 1
            # sharpStartIndicator.append(lineStr[0] == "#")
            # sharpEndIndicator.append(lineStr[-1] == "#")
            # print(lineStr)

    # startChar = processIndicator(sharpStartIndicator)
    # endChar = processIndicator(sharpEndIndicator)

    # return arrangements, startChar, endChar
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
    print(line)
    permCount = countArrangements(sharpPart, numbers)

    # permCount, startChar, endChar = countArrangements(sharpPart, numbers)
    # match endChar:
    #     case "#":   # joining chars are all . so just take the 5th power
    #         permCount = np.power(permCount1, 5)
    #     case ".":   # count the joining ? on the left side instead
    #         permCount2, _, _ = countArrangements("?" + sharpPart, numbers)
    #         permCount = permCount1 * np.power(permCount2, 4)
    #     case "?":   # start evaluating the other 4 immediately at the ?
    #         permCount2, _, _ = countArrangements(sharpPart + "?", numbers)
    #         permCount = permCount1 * np.power(permCount2, 4)
    #     case _:
    #         raise ValueError(f"Unreachable state: char is {endChar}")

    permCounts.append(permCount)

    pass


print(np.sum(permCounts))
# part 2
# 1145301219171 too low

