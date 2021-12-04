import re

#Read Lines and organize into list: numberslist
file_handle = open("input.txt", "r")
_numberslist = file_handle.readlines()
pattern = r"\n"
numberslist = [int(re.sub(pattern, "", numbers)) for numbers in _numberslist]
#print("Numbers: \n", numberslist)

#---Part 1---
compare_1 = tuple(zip(numberslist, numberslist[1:])) 
print("Part 1: ", len([item for item in compare_1 if (item[1] > item[0])]))

#---Part 2---
_compare_2 = tuple(zip(numberslist, numberslist[1:], numberslist[2:]))
compare_2 = [sum(listy) for listy in _compare_2]
print("Part 2: ", len([compare_2[i] for i in range(len(compare_2)) if i > 0 and compare_2[i] > compare_2[i-1]]))