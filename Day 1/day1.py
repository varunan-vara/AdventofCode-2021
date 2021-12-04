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

numberslist = [int(item) for item in itemlist]

#---Part 1---
compare_1 = tuple(zip(numberslist, numberslist[1:])) 
print("Part 1: ", len([item for item in compare_1 if (item[1] > item[0])]))

#---Part 2---
_compare_2 = tuple(zip(numberslist, numberslist[1:], numberslist[2:]))
compare_2 = [sum(listy) for listy in _compare_2]
print("Part 2: ", len([compare_2[i] for i in range(len(compare_2)) if i > 0 and compare_2[i] > compare_2[i-1]]))