#!/usr/bin/env python
#Curvy Litte Bottles
from math import *
from sys import *

def evalintegral(poly,start,stop):
    result = 0.0
    for i in range(len(poly)):
        result += (poly[i]*stop**i - poly[i]*start**i)
    return pi*result

def square(poly):
    result = [0]*(len(poly)*2 -1)
    for i in range(len(poly)):
        for j in range(len(poly)):
            result[i+j] += poly[i]*poly[j]
    return result
            

        
case = 0
while(True):
    case += 1 
    line = stdin.readline().strip()
    if line == "":
        break
    degree = int(line)
    coeffs = map(float,stdin.readline().split())
    data = stdin.readline().split()
    start = float(data[0])
    stop = float(data[1])
    inc = int(data[2])
    rsquared = square(coeffs)
    integral = [0]*(len(rsquared)+1)
    for i in range(len(rsquared)):
        integral[i+1] = (((rsquared[i])/(float(i+1))))
    volume = evalintegral(integral,start,stop) 
    print "Case " + str(case) + ": {0:.2f} ".format(volume)
    marks = [start]
    for i in range(1,9):
        target = i*inc
        guess = stop
        shift = (stop-marks[i-1])/2
        cmpval = target - evalintegral(integral, start, guess)
        if (cmpval > 0):
            if (i == 1):
                stdout.write("insufficient volume")
            break
            
        while (abs(cmpval) > .0001):
            if cmpval < 0:
                guess -= shift
            if cmpval > 0:
                guess += shift
            cmpval = target - evalintegral(integral, start, guess)
            shift /= 2
        if (evalintegral(integral, start, guess) > volume):
            break
        marks.append(guess)
        stdout.write("{0:.2f} ".format(guess-start))

    print 


