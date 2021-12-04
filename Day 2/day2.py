import re
import os

#Read Lines and organize into list: numberslist
here = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(here, "input.txt")
file_handle = open(file, "r")
_itemlist = file_handle.readlines()
pattern = r"\n"
itemlist = [re.sub(pattern, "", numbers) for numbers in _itemlist]
#print("Numbers: \n", numberslist)

inputlist = [item.split(" ") for item in itemlist]
inputlist = [[item[0], int(item[1])] for item in inputlist]

def locator (direction, listy):
    return [item[1] for item in listy if item[0] == direction]

def addingTo (inputy, direction, multiplier):
    return inputy[1] * multiplier if (inputy[0] == direction) else 0

#---Part 1---
forward = sum(locator("forward", inputlist))
depth = sum(locator("down", inputlist)) - sum(locator("up", inputlist))
print("Part 1: ", forward * depth)

#---Part 2---
aim = 0
depth = 0
forward = 0
for instruction in inputlist:
    aim += addingTo(instruction, "down", 1)
    aim -= addingTo(instruction, "up", 1)
    depth += addingTo(instruction, "forward", aim)
    forward += addingTo(instruction, "forward", 1)
print("Part 2: ", depth * forward)