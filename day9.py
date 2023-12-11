import numpy as np

with open("input/day9.txt") as day9:
    lines = day9.readlines()

def getNextPart1(numbers):
    currentNumbers = np.copy(numbers)
    endNumbers = [currentNumbers[-1]]
    while currentNumbers[0] != 0 or np.prod(currentNumbers) != np.sum(currentNumbers):
        diffs = np.diff(currentNumbers)
        endNumbers.append(diffs[-1])
        currentNumbers = diffs
    newEnd = 0
    del endNumbers[-1]
    for endNumber in reversed(endNumbers):
        newEnd = endNumber + newEnd
    return newEnd

def getNextPart2(numbers):
    currentNumbers = np.copy(numbers)
    startNumbers = [currentNumbers[0]]
    while currentNumbers[0] != 0 or np.prod(currentNumbers) != np.sum(currentNumbers):
        diffs = np.diff(currentNumbers)
        startNumbers.append(diffs[0])
        currentNumbers = diffs
    newStart = 0
    del startNumbers[-1]
    for startNumber in reversed(startNumbers):
        newStart = startNumber - newStart
    return newStart

nextNumbers = []

for line in lines:
    numbers = [int(x) for x in line.split()]
    nextNumber = getNextPart2(numbers)
    nextNumbers.append(nextNumber)

print(np.sum(nextNumbers))
# 1923424291 too low
# 453 too low (part two)
