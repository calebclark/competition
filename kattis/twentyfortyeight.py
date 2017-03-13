#!/usr/bin/env python
# 2048
from copy import *
from sys import *
from math import *

# the direction
dr = 0
grid = []


def inttuple(intstr):
    integer = int(intstr)
    return [int(integer), True]

def nextsquare(y,x):
    if dr is 0:
        return (y,x-1)
    elif dr is 1:
        return (y-1,x)
    elif dr is 2:
        return (y,x+1)
    elif dr is 3:
        return (y+1,x)
def isvalid(y,x):
    if x > 3 or y > 3 or x < 0 or y < 0:
        return False
    if grid[y][x][1] == False:
        return False
    return True


for i in range(4):
    grid.append(map(inttuple,stdin.readline().split()));


dr = int(stdin.readline()) 
if dr == 2:
    xcrange = range(3,-1,-1)
else:
    xcrange = range(4)
if dr == 3:
    ycrange = range(3,-1,-1)
else:
    ycrange = range(4)

for i in ycrange:
    for j in xcrange:
        if not isvalid(i,j):
            continue
        nextsq = nextsquare(i,j)
        val = grid[i][j][0]
        prev = (i,j)
        while isvalid(nextsq[0], nextsq[1]):
            if grid[nextsq[0]][nextsq[1]][0] == 0:
                grid[nextsq[0]][nextsq[1]][0] = val
                grid[prev[0]][prev[1]][0] = 0
                prev = deepcopy(nextsq)
                nextsq = nextsquare(nextsq[0],nextsq[1])
            elif grid[nextsq[0]][nextsq[1]][0] == val and\
            grid[nextsq[0]][nextsq[1]][1] == True:
                grid[nextsq[0]][nextsq[1]][0] = val*2
                grid[nextsq[0]][nextsq[1]][1] = False
                grid[prev[0]][prev[1]][0] = 0
                break
            else: 
                break
                
for i in range(4):
    for j in range(4):
        stdout.write(str(grid[i][j][0]) + " ")
    print
