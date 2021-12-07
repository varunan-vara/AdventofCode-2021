import re
import os

#Read Lines and organize into list: numberslist
here = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(here, "input.txt")
file_handle = open(file, "r")
_itemlist = file_handle.readlines()
pattern = r"\n"
itemlist = [re.sub(pattern, "", numbers) for numbers in _itemlist]
#print("Numbers: \n", itemlist)

newlist = [[char for char in item] for item in itemlist]
x = len(newlist[0])
#posi() returns a True boolean if the value in that position in the diagnostics has more 1 than 0
def posi (p):
    return sum([int(item[p]) for item in newlist]) * 2 >= len(newlist)

#---Part 1---
gamma = "".join([("1" if posi(i) else "0") for i in range(x)])
epsilon = "".join([("0" if posi(i) else "1") for i in range(x)])

print("Part 1:", int(gamma, 2) * int(epsilon,2))

#---Part 2---
# Function that grabs most common value in position
def maxnum (listy, x):
    returnlist = [item[x] for item in listy]
    nums = {"0":0, "1":0}
    for item in set(returnlist):
        nums[item] = returnlist.count(item)
    if nums["1"] >= nums["0"]: return "1"
    else: return "0"

oxygen = co2 = itemlist
x = y = 0
#This is messy because the previous for loop did not work
while(x < len(oxygen[0])):
    templist = []
    maxy = maxnum(oxygen,x)
    for item in oxygen:
        if (item[x] == maxy):
            templist.append(item)
    oxygen = templist
    x += 1

while(y < len(co2[0]) and len(co2) > 1):
    templist = []
    maxy = int(maxnum(co2,y))
    print(maxy)
    for item in co2:
        if (int(item[y]) != maxy):
            templist.append(item)
    co2 = templist
    y += 1
print(oxygen)
print(co2)
print(int(oxygen[0],2) * int(co2[0],2)) if len(oxygen) == 1 and len(co2) == 1 else print("Error - More than one output")