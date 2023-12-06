import numpy as np


with open("input/day1.txt") as day1:
    lines = day1.readlines()

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

def rotate(string, length, char):
    if len(string) < length:
        return string + char
    return string[1-length:] + char

def fixstringtoohigh(string):
    last3chars = ""
    last4chars = ""
    last5chars = ""
    outstring = string
    for char in string:
        last3chars = rotate(last3chars, 3, char)
        last4chars = rotate(last4chars, 4, char)
        last5chars = rotate(last5chars, 5, char)
        # do in reverse order because the last 5 started earlier than last 4
        if last5chars in digits5:
            outstring = outstring.replace(last5chars, digits5[last5chars], 1)
        elif last4chars in digits4:
            outstring = outstring.replace(last4chars, digits4[last4chars], 1)
        elif last3chars in digits3:
            outstring = outstring.replace(last3chars, digits3[last3chars], 1)
    return outstring

def fixstringtoolow(string):
    digits = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for name, digit in digits.items():
        string.replace(name, digit)
    return string

def firstdigit(string):
    for char in string:
        if char.isdigit():
            return char

values = []

for line in lines:
    line = fixstring(line)
    valueStr = firstdigit(line) + firstdigit(line[::-1])
    value = int(valueStr)
    values.append(value)

print(np.sum(values))
