#!/usr/bin/env python
# A Rational Sequence
from sys import *
from math import *


n = int(stdin.readline())

def isright((num,denom)):
    return num > denom

# takes a left child and return it's right sibling
def getrightsibling((num,denom)):
        pnum,pdenom = getparent((num,denom))
        snum = pnum + pdenom
        sdenom = pdenom
        return (snum,sdenom)
def getrightchild((num,denom)):
    return (num+denom,denom)
def getleftchild((num,denom)):
    return (num,num+denom)

def getparent((num,denom)):
    if num == denom:
        pnum = 1
        pdenom = 1
    # left children
    elif not isright((num,denom)):
        pnum = num
        pdenom = denom - num 
    else:
        pnum = num - denom
        pdenom = denom
    return (pnum,pdenom)

def getnext((num,denom)):
    if (num == denom):
        rnum = 1
        rdenom = 2
    elif not isright((num,denom)):
        rnum,rdenom = getrightsibling((num,denom))
    else:
        rootd = denom
        rootn = num % denom
        heightdiff = num/denom
        (rootsibn,rootsibd) = getrightsibling((rootn,rootd))
        rnum = rootsibn
        rdenom = rootsibd + (rootsibn * heightdiff)
         
    return (rnum,rdenom)




for i in range(n):
    num,denom = map(int,stdin.readline().strip().split(" ")[1].split("/"))
    print str(i+1)+" ",
    rnum,rdenom = getnext((num,denom))
    print str(rnum) + "/" + str(rdenom)

