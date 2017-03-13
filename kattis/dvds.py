#!/usr/bin/env python
# DVDs
from sys import *
from math import *


k = int(stdin.readline())
for i in range(k):
    n = int(stdin.readline())
    dvds = map(int,stdin.readline().split())
    topordered = 0
    for j in dvds:
        if j == topordered +1:
            topordered += 1
    print n-topordered

