#!/usr/bin/env python
from sys import *
from math import *

def isTriangle(a,b):
    if (a[0] == 0 and a[1] == 0) or (b[0] == 0 and b[1] == 0):
        return False
    elif a[1] == b[1] == 0:
        return False
    elif a[1] == 0 or b[1] == 0:
        return True
    elif abs((float(a[0])/float(a[1])) - (float(b[0])/float(b[1]))) < .0000001:
        return False
    else: 
        return True





n = int(stdin.readline())
for i in range(n):
    stdout.write("Case #" + str(i+1) + ": ");
    nums = map(int, stdin.readline().split())
    a = (nums[2] - nums[0], nums[3] - nums[1])
    b = (nums[4] - nums[0],nums[5] - nums[1])
    if not(isTriangle(a,b)):
        print "not a triangle"
        continue

    s1 =sqrt(a[0]**2 + a[1]**2) 
    s2 = sqrt(b[0]**2 + b[1]**2)
    s3 = sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    if  s1 == s2 or s2 == s3 or s3 == s1:
        stdout.write("isosceles ");
    else:
        stdout.write("scalene ");

    if s1 > s2:
        if s1 > s3:
            big = s1
            small1 = s2
            small2 = s3
        else:
            big = s3
            small1 = s1
            small2 = s2
    else:
        if s2 > s3:
            big = s2
            small1 = s1
            small2 = s3
        else:
            big = s3
            small1 = s1
            small2 = s2
    
    cmpval = big**2 - (small1**2 + small2**2) 
    if cmpval < .00001 and cmpval > -.000001:
        print "right triangle"
    elif cmpval < 0:
        print "acute triangle"
    else: 
        print "obtuse triangle"





