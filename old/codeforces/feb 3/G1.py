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
    n, c = mp()
    # print(n, c)
    l = li()
    x = -1
    tps = 0

    for i in range(n):
        if x != -1:
            if l[i] != 0:
                if l[i] < c:
                    c = c - l[i]
                    l[i] = 0
                    x = -1
                    tps += 1
        else:
            c -=1
            x += 1

    print(tps)

            









    
    # ---- CHECK FOR CORNER CASES ----
    
for _ in range(inp()):
    solve()