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
    n = inp()
    x = []
    for i in range(n):
        temp = li()
        x.append(temp)
    max = x[0][0]
    for i in x:
        if i[0] == max:
            max = i[0]
        else:
            max = i[0]

    for i in x:
        if i[0] != max:
            res = i

    res.insert(0, max)
    printCleanList(res)








    
    # ---- CHECK FOR CORNER CASES ----
    
for _ in range(inp()):
    solve()