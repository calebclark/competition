#!/usr/bin/env python3
from sys import stdin
from math import ceil
from math import sqrt

t = int(stdin.readline())

def convert(x,j,w,e):
    if x > 0 and j>0:
        return e
    if x < 0 and j>0:
        return w
    if x > 0 and j<0:
        return w
    if x < 0 and j<0:
        return e

for i in range(t):
    # get x and y
    x,y = map(int,stdin.readline().split())
    #print(str(x)+", "+str(y))
    ax = abs(x)
    ay = abs(y)
    # find the absolute value of the sum of x and y
    sum_abs = ax + ay

    # find the optimal way to reach sum_abs on the pogo stick

    # sum abs is between the (n-1)st and nth triangular numbers (exclusive, inclusive)
    n = int(ceil(-.5 + sqrt(.5**2 - 4*.5*(-1*sum_abs))))
    nth_triangular = int((n*(n+1))/2)
    diff = int(nth_triangular - sum_abs)
    components = []
    for k in range(1,n+1):
        components.append(k)
    if diff % 2 == 1:
        components.append((n+1))
        diff += n+1
        if diff % 2 == 1:
            components.append((n+2)*-1)
            diff += (n+2)*-1

    if diff > 0:
        components[diff//2-1] = components[diff//2-1]*-1
    #print(components)
    # find a subset of components that sums to min(ax,ay)
    z = min(ax,ay)
    if z != 0:
        z_comp = []
        z_complement = []
        for k in components:
            z_complement.append(k)
        z_sum = 0
        j = len(components) - 1
        while z_sum+components[j] < z:
            if components[j] > 0:
                z_comp.append(components[j])
                z_sum += components[j]
                z_complement.remove(components[j])
            j -= 1
        
        z_diff = z - z_sum
        z_comp.append(components[z_diff-1])
        z_complement.remove(components[z_diff-1])
        if components[z_diff-1] < 0:
            z_comp.append(components[z_diff])
            z_comp.append(components[z_diff-2])
            z_complement.remove(components[z_diff])
            z_complement.remove(components[z_diff-2])
        if min(ax,ay)==ax:
            x_comp = z_comp
            y_comp = z_complement
        else:
            x_comp = z_complement
            y_comp = z_comp
        #print(x_comp)
        #print(y_comp)
    output = "Case #" + str(i+1) + ": "
    if x==0:
        for j in components:
            output+=convert(y,j,"S","N")
    elif y == 0:
        for j in components:
            output+=convert(x,j,"W","E")
    else:
        for j in components:
            if j in x_comp:
                output+=convert(x,j,"W","E")
            if j in y_comp:
                output+=convert(y,j,"S","N")
    print(output)
