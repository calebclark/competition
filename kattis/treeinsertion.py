#!/usr/bin/env python
# Tree Insertion
from math import *
from sys import *


def numtrees(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1
    root = nums[0]
    left = []
    right = []
    for i in nums[1:]:
        if i < root:
            left.append(i)
        else:
            right.append(i)
        k



while True:
    n = stdin.readline().strip()
    if n == "":
        break 
    n = int(n) 
    nums = map(int,stdin.readline().split())
    print numtrees(nums)
