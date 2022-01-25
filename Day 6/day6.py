import re
import os
import time

#Read Lines and organize into list: numberslist
here = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(here, "input.txt")
file_handle = open(file, "r")
_itemlist = file_handle.readlines()
pattern = r"\n"
itemlist = [re.sub(pattern, "", numbers) for numbers in _itemlist]
#print("Numbers: \n", itemlist)
fishes = itemlist[0].split(",")
for i in range(len(fishes)):
    fishes[i] = int(fishes[i])
print("Initial State: " + str(fishes))

counter = 0
while counter <= 80:
    for i in range(len(fishes)):
        fishes[i] -= 1
        if fishes[i] < 0:
            fishes[i] = 6
            fishes.append(8)
    counter += 1
    print("After " + str(counter) + " days: " + str(fishes))
print(len(fishes))