#!/usr/bin/env python
# 10 Kinds of People
from math import *
from sys import *

grid = []
paths = []
getset = {}
def getkind(p):
    return grid[p[0]][p[1]]

def recadd(p, id, lastkind="42"):
    if p in getset:
        #print (p,1)
        return
    if (p[0] not in range(rows)) or (p[1] not in range(cols)):
        #print (p,2)
        return
    kind = getkind(p)
    #print ("kind",kind)
    if (lastkind == "42") or (kind == lastkind):
        getset[p] = id
        recadd((p[0]+1,p[1]),id,kind)
        recadd((p[0]-1,p[1]),id,kind)
        recadd((p[0],p[1]+1),id,kind)
        recadd((p[0],p[1]-1),id,kind)

#line0 = stdin.readline().split()
#rows = int(line0[0])
#cols = int(line0[1])
#don't be a scrub
rows,cols=map(int,stdin.readline().split())
for i in range(rows):
    grid.append(list(stdin.readline()))

n = int(stdin.readline())
setnum = 0
for i in range(n):
    data = map(int,stdin.readline().split())
    paths.append([(data[0]-1,data[1]-1),(data[2]-1,data[3]-1)])
for i in range(rows):
    for j in range(cols):
        p = (i,j)
        recadd(p,setnum)
        setnum += 1

        
print getset
for [p1,p2] in paths:
    if getset[p1] is getset[p2]:
        if getkind(p1) is "1":
            print "decimal"
        if getkind(p1) is "0":
            print "binary"
    else:
        print "neither"

