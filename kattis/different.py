#!/usr/bin/env python
# A different problem
from sys import *
from math import *

line = stdin.readline()
while(line.strip() != ""):
    nums = map(int,line.split())
    print abs(nums[0] - nums[1])
    line = stdin.readline()
    
