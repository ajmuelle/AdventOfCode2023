import numpy as np

with open("input/day2.txt") as day2:
    lines = day2.readlines()

def getColor(roundStr, color):
    colorStrings = roundStr.split(", ")
    for colorStr in colorStrings:
        if f" {color}" in colorStr:
            return int(colorStr.split(f" {color}")[0])
    return 0

class Round:
    def __init__(self, roundStr):
        self.red = getColor(roundStr, "red")
        self.green = getColor(roundStr, "green")
        self.blue = getColor(roundStr, "blue")
    def __gt__(self, other):
        """If any of self is greater than any of other, return True"""
        return self.red > other.red or self.green > other.green or self.blue > other.blue

class Game:
    def __init__(self, gameStr):
        idString, roundPart = gameStr.split(": ")

        self.gameID = int(idString.split("Game ")[1])
        self.rounds = []

        roundStrings = roundPart.split("; ")
        for roundStr in roundStrings:
            self.rounds.append(Round(roundStr))

        self.maxColors = Round("")
        for round in self.rounds:
            if round.red > self.maxColors.red:
                self.maxColors.red = round.red
            if round.green > self.maxColors.green:
                self.maxColors.green = round.green
            if round.blue > self.maxColors.blue:
                self.maxColors.blue = round.blue

        powerMulticands = [self.maxColors.red, self.maxColors.green, self.maxColors.blue]

        # if one of the max colors is 0, exclude it from multiplication
        for multiplicand in powerMulticands:
            if multiplicand == 0:
                del multiplicand

        self.power = np.prod(powerMulticands)

possibleGames = []  # part 1
powers = []         # part 2

part1colors = Round("12 red, 13 green, 14 blue")

for line in lines:
    game = Game(line)
    # maxColors = game.getMaxColors()
    # if maxColors > part1colors:
    #     continue
    # possibleGames.append(game.gameID)
    powers.append(game.power)

# PART ONE
# print(np.sum(possibleGames))

# PART TWO
print(np.sum(powers))
