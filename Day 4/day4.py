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


bingonums = itemlist[0]
bingonums = bingonums.split(",")
itemlist.pop(0)

itemlist = [item.split(" ") for item in itemlist if item]
templist = []
item2list = []
for item in itemlist:
    item = [num for num in item if num]
    for thing in item:
        templist.append(thing)
    if (len(templist) >= 25):
        item2list.append(templist)
        templist = []
itemlist = item2list

won = False

class bingo_card :
    def __init__ (self, bingonums):
        bingodicty = {}
        for i in range(25):
            pos = chr(ord('@')+(i // 5) + 1) + str((i % 5) + 1)
            bingodicty[pos] = bingonums[i]
        self.bingodict = bingodicty
        self.selected = []
        self.lastnum = ""
        self.won = False
        self.score = 0
    def returnbingo (self, val):
        return self.bingodict[val]
    def returnbingosheet (self):
        return self.bingodict
    def isWinner (self, printbool = True):
        counter = {
            "A": 0,
            "B": 0,
            "C": 0,
            "D": 0,
            "E": 0,
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0
        }
        for marked in self.selected:
            counter[marked[0]] += 1
            counter[marked[1]] += 1
        
        A1 = ("A1" in self.selected)
        B2 = ("B2" in self.selected)
        C3 = ("C3" in self.selected)
        D4 = ("D4" in self.selected)
        E5 = ("E5" in self.selected)
        A5 = ("A5" in self.selected)
        B4 = ("B4" in self.selected)
        D2 = ("D2" in self.selected)
        E1 = ("E1" in self.selected)
        if (5 in counter.values() or (A1 and B2 and C3 and D4 and E5) or (A5 and B4 and C3 and D2 and E1)):
            self.won = True
            score = 0
            for val in self.bingodict.keys():
                if val not in self.selected:
                    score += int(self.bingodict[val])
            if printbool:
                print("Card Won!")
                print(card.printselected())
                print(int(self.lastnum) * int(score))
            self.score = int(self.lastnum) * int(score)
    def inputnum (self, num):
        if (num in self.bingodict.values()):
            keylist = list(self.bingodict.keys())
            vallist = list(self.bingodict.values())
            key = vallist.index(num)
            if (keylist[key] not in self.selected): self.selected.append(keylist[key])
        self.lastnum = num
    def printselected (self):
        return self.selected
    def wonbool (self):
        return self.won
    def returnscore (self):
        return self.score
bingo_card_list = [bingo_card(item) for item in itemlist]
print(len(bingo_card_list))
#---Part 1---
numcount = 0
while not won:
    breakval = False
    for card in bingo_card_list:
        card.inputnum(bingonums[numcount])
        card.isWinner(False)
    for card in bingo_card_list:
        if card.wonbool():
            print("Part 1:", card.returnscore())
            won = True
    numcount += 1
print(len(bingo_card_list))
#---Part 2---
#Rewrite bingocards class

class BingoCards:
    def __init__ (self, card:list):
        tempbingocard = []
        temprow = []
        for number in card:
            temprow.append(number)
            if len(temprow) >= 5:
                tempbingocard.append(temprow)
                temprow = []
        bingo = {}
        for i in range(len(tempbingocard)):
            bingo[chr(i + 96)] = tempbingocard[i]
        self.card = bingo
        self.turnssurvived = 0
        self.tickedvals = []
    def isSolved (self):
        return
    def numinput (self, num):
        for key in self.card:
            if num in self.card[key]:
                x = self.card[key].index(num)
                foundval = key + str(x)
                print("Found value in bingocard: " + foundval)
                self.tickedvals.append(foundval)
        self.isSolved()

bingo_card_list = [BingoCards(item) for item in itemlist]
print(itemlist)
print(bingo_card_list[0].card)
print("Part 2:")
