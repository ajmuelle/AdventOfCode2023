import numpy as np

with open("input/day3.txt") as day3:
    lines = day3.readlines()

numbers2d = []
isNumber = False
currentStr = ""

for line in lines:
    numbers = []
    for index, char in enumerate(line):
        if char.isdigit():
            currentStr += char
        elif currentStr:
            numbers.append((index - len(currentStr), int(currentStr)))
            currentStr = ""
    numbers2d.append(numbers)

for rowIndex, numbers in numbers2d
