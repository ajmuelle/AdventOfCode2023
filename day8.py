import numpy as np

with open("input/day8.txt") as day8:
    lines = day8.readlines()

# convert left/right to indices
leftRightMap = {"L": 0, "R": 1}
leftRightList = [leftRightMap[letter] for letter in lines[0][:-1]]

del lines[0:2]

letterTripleMap = {}
for line in lines:
    key, value = line.split(" = ")
    values = value.replace("\n", "")[1:-1].split(", ")
    letterTripleMap[key] = values

currentValue = "AAA"
count = 0
while currentValue != "ZZZ":
    currentDirection = leftRightList[count % len(leftRightList)]
    currentValue = letterTripleMap[currentValue][currentDirection]
    count += 1

print(count)
