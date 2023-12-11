from enum import IntEnum

import numpy as np

with open("input/day7.txt") as day7:
    lines = day7.readlines()

letter2number = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 1,     # 11 in part 1
    "T": 10
}

class HandType(IntEnum):
    HIGHCARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6

def getHandType(cards):
    uniqueCards, cardCounts = np.unique(cards, return_counts=True)

    # for part 2
    if 1 in uniqueCards:
        match len(uniqueCards):
            case 1:
                # base case: hand is literally JJJJJ
                return HandType.FIVE_OF_A_KIND
            case 2:
                # J becomes the other card
                return HandType.FIVE_OF_A_KIND
            case 3:
                if 3 in cardCounts:
                    # 1 J pairs with 3 equal or 3 Js pair with 1 equal
                    return HandType.FOUR_OF_A_KIND
                elif cardCounts[0] == 2:
                    # 2 Js pair with 2 equal
                    return HandType.FOUR_OF_A_KIND
                else:
                    # 2 Js pair with 1 equal or 1 J pairs with 2 equal
                    return HandType.FULL_HOUSE
            case 4:
                # J always ends up in 3 group, because 3 of a kind > 2 pair
                return HandType.THREE_OF_A_KIND
            case _:
                # J pairs with the highest other card
                return HandType.ONE_PAIR

    # part 1 version
    match len(uniqueCards):
        case 1:
            return HandType.FIVE_OF_A_KIND
        case 2:
            if cardCounts[0] in [1, 4]:
                return HandType.FOUR_OF_A_KIND
            else:
                return HandType.FULL_HOUSE
        case 3:
            if 3 in cardCounts:
                return HandType.THREE_OF_A_KIND
            else:
                return HandType.TWO_PAIR
        case 4:
            return HandType.ONE_PAIR
        case _:
            return HandType.HIGHCARD

class Hand:
    def __init__(self, line):
        cardStr, bidStr = line.split(" ")
        self.bid = int(bidStr)
        self.cards = []

        for card in cardStr:
            if card.isdigit():
                self.cards.append(int(card))
            else:
                self.cards.append(letter2number[card])

        self.handType = getHandType(self.cards)

    def __gt__(self, other):
        if self.handType > other.handType:
            return True
        elif self.handType < other.handType:
            return False
        else:   # same hand type, must compare each card
            for myCard, otherCard in zip(self.cards, other.cards):
                if myCard > otherCard:
                    return True
                elif otherCard > myCard:
                    return False
            return False    # hopefully two equal hands are never compared

hands = [Hand(line) for line in lines]

handsArray = np.sort(hands)

winnings = [hand.bid * (index + 1) for index, hand in enumerate(handsArray)]

print(np.sum(winnings))
# 247837969 too high
