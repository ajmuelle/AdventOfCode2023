import numpy as np


with open("input/day1.txt") as day1:
    lines = day1.readlines()

# legacy map for incorrect solutions
digits = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

digits3 = {
    "one": "1",
    "two": "2",
    "six": "6",
}
digits4 = {
    "four": "4",
    "five": "5",
    "nine": "9"
}
digits5 = {
    "three": "3",
    "seven": "7",
    "eight": "8",
}

values = []

##### CORRECT SOLUTION #####

def goldilox(string):
    firstDigit = ""
    lastDigit = ""

    # look forward for first digit
    for index, char in enumerate(string):
        if char.isdigit():
            firstDigit = char
            break
        # check if it's the first letter of digit word
        elif char in ["o", "t", "f", "s", "e", "n"]:
            try:
                next3 = string[index:index+3]
                if next3 in digits3:
                    firstDigit = digits3[next3]
                    break

                next4 = string[index:index+4]
                if next4 in digits4:
                    firstDigit = digits4[next4]
                    break

                next5 = string[index:index+5]
                if next5 in digits5:
                    firstDigit = digits5[next5]
                    break

            except IndexError:
                pass

    # look backward for last digit
    index = len(string) - 1
    while index >= 0:   # while loop makes it easier to keep a forward index
        char = string[index]
        if char.isdigit():
            lastDigit = char
            break
        # check if it's the last letter of digit word
        elif char in ["e", "o", "r", "x", "n", "t"]:
            try:
                prev3 = string[index-2:index+1]
                if prev3 in digits3:
                    lastDigit = digits3[prev3]
                    break

                prev4 = string[index-3:index+1]
                if prev4 in digits4:
                    lastDigit = digits4[prev4]
                    break

                prev5 = string[index-4:index+1]
                if prev5 in digits5:
                    lastDigit = digits5[prev5]
                    break

            except IndexError:
                pass
        index -= 1

    outstring = f"{firstDigit}{lastDigit}"
    return outstring

for line in lines:
    valueStr = goldilox(line)
    value = int(valueStr)
    values.append(value)

print(np.sum(values))

##### INCORRECT SOLUTION 1: TOO LOW #####

def fixstringtoolow(string):
    for name, digit in digits.items():
        string.replace(name, digit)
    return string

def firstdigit(string):
    for char in string:
        if char.isdigit():
            return char

# for line in lines:
#     line = fixstringtoolow(line)
#     valueStr = firstdigit(line) + firstdigit(line[::-1])
#     value = int(valueStr)
#     values.append(value)
#
# print(np.sum(values))

##### INCORRECT SOLUTION 2: TOO HIGH #####

def rotate(string, length, char):
    if len(string) < length:
        return string + char
    return string[1-length:] + char

def fixstringtoohigh(string):
    last3chars, last4chars, last5chars = "", "", ""
    words = []
    for char in string:
        last3chars = rotate(last3chars, 3, char)
        last4chars = rotate(last4chars, 4, char)
        last5chars = rotate(last5chars, 5, char)
        # do in reverse order because the last 5 started earlier than last 4
        if last5chars in digits5:
            words.append(last5chars)
            last5chars = ""     # flush the buffer to avoid 'twone' situation
        elif last4chars in digits4:
            words.append(last4chars)
            last4chars = ""
        elif last3chars in digits3:
            words.append(last3chars)
            last3chars = ""
    for word in words:
        # replace exactly one occurrence so we don't get ahead of ourselves
        string = string.replace(word, digits[word], 1)
    return string

# for line in lines:
#     line = fixstringtoohigh(line)
#     valueStr = firstdigit(line) + firstdigit(line[::-1])
#     value = int(valueStr)
#     values.append(value)
#
# print(np.sum(values))

