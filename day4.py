import numpy as np

with open("input/day4.txt") as day4:
    lines = day4.readlines()

scores = []

for line in lines:
    cardPart, numbersPart = line.split(":")
    winningStr, myStr = numbersPart.split("|")
    winningNumbers = [int(num) for num in winningStr.split()]
    myWins = []
    for num in myStr.split():
        if int(num) in winningNumbers:
            myWins.append(int(num))
    if len(myWins) > 0:
        score = int(2 ** (len(myWins) - 1))
        scores.append(score)

print(np.sum(scores))
