from re import L
import sys
import os.path
from math import *
from bisect import *
from itertools import *
from collections import defaultdict as dd, Counter
from itertools import accumulate
from operator import add
#from sortedcontainers import SortedList as SL, SortedSet as SS, SortedDict as SD

if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")

def st():
    return str(sys.stdin.buffer.readline().strip())[2:-1]
def li():
    return list(map(int, sys.stdin.buffer.readline().split()))
def mp():
    return map(int, sys.stdin.buffer.readline().split())
def inp():
    return int(sys.stdin.buffer.readline())

def printCleanList(x):
    print(*x, sep=" ")

mod = 1000000007
INF = float("inf")

def solve():
    # print()
    n, s, r = mp()
    res = [0] * (n-1)
    res.append(s-r)
    thing = s-r
    # s = s - thing
    # r = r - thing
    for i in range(n-1):
        res[i] = 1
        r = r-1
    i = 0
    while r!=0:
        if(res[i]<thing):
            res[i] += 1
            r = r - 1
        else:
            i += 1
    
    # n = n - 1
    # while n!=0:
    #     if s%n == 0:
    #         res.append(s//n)
    #         thing = s//n
    #     else:
    #         res.append(s%n)
    #         thing = s%n
    #     n = n - 1
    #     s = s - thing

    printCleanList(res)
        







    
    # ---- CHECK FOR CORNER CASES ----
    
for _ in range(inp()):
    solve()