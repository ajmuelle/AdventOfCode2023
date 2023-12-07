import numpy as np

with open("input/day2.txt") as day2:
    lines = day2.readlines()

##### PART ONE SOLUTION #####

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

    def getMaxColors(self):
        maxColors = Round("")
        for round in self.rounds:
            if round.red > maxColors.red:
                maxColors.red = round.red
            if round.green > maxColors.green:
                maxColors.green = round.green
            if round.blue > maxColors.blue:
                maxColors.blue = round.blue
        return maxColors

# games = []
# maxColorsByGame = []

possibleGames = []

part1colors = Round("12 red, 13 green, 14 blue")

for line in lines:
    game = Game(line)
    maxColors = game.getMaxColors()
    if maxColors > part1colors:
        continue
    possibleGames.append(game.gameID)
    # games.append(game)
    # maxColorsByGame.append(game.getMaxColors())

print(np.sum(possibleGames))
