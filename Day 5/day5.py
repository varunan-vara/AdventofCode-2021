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

class Vent:
    def __init__ (self, ventinput:str):
        ventcoords = ventinput.split(" -> ")
        ventcoords = [item.split(",") for item in ventcoords]
        newcoords = []
        for item in ventcoords:
            returnlist = []
            for val in item:
                returnlist.append(int(val))
            newcoords.append(returnlist)
        self.coords = newcoords
        # print(self.coords)
        changex = newcoords[1][0] - newcoords[0][0]
        changey = newcoords[1][1] - newcoords[0][1]
        if changex == 0:
            self.direction = "vertical"
        if changey == 0:
            self.direction = "horizontal"
        if abs(changex) == abs(changey):
            self.direction = "diagonal"
        # print(self.direction)
    def actedcoords (self):
        if self.direction == "vertical":
            yvals = [self.coords[0][1], self.coords[1][1]]
            return [[self.coords[0][0], i] for i in range(min(yvals), max(yvals) + 1)]
        if self.direction == "horizontal":
            xvals = [self.coords[0][0], self.coords[1][0]]
            return [[i, self.coords[0][1]] for i in range(min(xvals), max(xvals) + 1)]
        if self.direction == "diagnoal":
            xvals = []
            return
ventlist = [Vent(item) for item in itemlist]
tickcoords = []
for line in ventlist:
    if line.direction != "diagonal":
        for value in line.actedcoords():
            tickcoords.append(value)
yvals = [item[1] for item in tickcoords]
xvals = [item[0] for item in tickcoords]

maxx = max(xvals)
print("maxx = ", maxx)
maxy = max(yvals)
print("maxy = ", maxy)
grid = [[0] * (maxy + 1)] * (maxx + 1)

for coord in tickcoords:
    print(coord)
    grid[coord[0]][coord[1]] += 1

counter = 0
for xs in grid:
    for ys in xs:
        if ys > 1:
            counter +=1
print(counter)