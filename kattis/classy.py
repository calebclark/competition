#!/usr/bin/env python
# A Classy Problem
from math import *
from sys import *
numcases = int(stdin.readline())
for c in range(numcases):
    people = []
    numpeople = int(stdin.readline())
    for p in range(numpeople):
        data = stdin.readline().split()
        name = data[0][0:-1]
        sclass = data[1].split("-")
        sclass.reverse()
        numclass = 0
        for i in range(15):
            numclass *= 10
            if i >= len(sclass):
                numclass += 2
                continue
            dig = sclass[i]
            if dig== "upper":
                numclass += 1
            elif dig == "middle":
                numclass += 2
            else:
                numclass += 3
        people.append((numclass,name))
    people.sort()
    for i in people:
        print i[1]
    print "="*30



        


