#!/usr/bin/env python 
from sys import stdin
from math import log, floor
n = stdin.readline()
for i in range(int(n)):
    data = stdin.readline().split()
    frombase = len(data[1])
    tobase = len(data[2])
    numlist = []  
    for digit in data[0]:
        numlist.append( data[1].find(digit))
    num = 0;
    for k in range(0,len(numlist)):
        num += numlist[len(numlist)-k-1]*pow(frombase,k)
    result = ""
    while num != 0:
       result  = str(data[2][int(num)%tobase]) + result;
       num /= tobase
    print "Case #" + str(i+1) + ": " + result

