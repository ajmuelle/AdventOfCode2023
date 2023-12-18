import numpy as np

with open("input/day15.txt") as day15:
    # for once, just read the whole file, don't split into lines
    line = day15.read()

def hash(string):
    currentValue = 0
    for char in string:
        ascii = ord(char)
        currentValue += ascii
        currentValue *= 17
        currentValue %= 256
    return currentValue

sequence = line.split(",")

##### PART ONE #####
# hashes = []
# for step in sequence:
#     # print(f"{step} {hash(step)}")
#     hashes.append(hash(step))
#
# print(np.sum(hashes))

##### PART TWO #####
# unstable implementation, relies on dict keys maintaining order
boxes = [{} for x in range(256)]
for step in sequence:
    if "=" in step:
        # add or replace lens
        label, focalStr = step.split("=")
        focalLen = int(focalStr)
        boxNum = hash(label)
        boxes[boxNum][label] = focalLen
    else:
        # remove a lens
        label = step.split("-")[0]
        boxNum = hash(label)
        boxes[boxNum].pop(label, None)

focusingPowers = []
for boxIndex, box in enumerate(boxes):
    boxNum = boxIndex + 1
    slotNum = 1
    for lens, focalLen in box.items():
        focusingPower = boxNum * slotNum * focalLen
        focusingPowers.append(focusingPower)
        slotNum += 1

print(np.sum(focusingPowers))
