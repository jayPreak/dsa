from functools import reduce
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

def printListToStr(x):
    print(*x, sep="")

mod = 1000000007
INF = float("inf")

def solve():
    n = inp()
    l = li()

    for x in range(28):
        b =[ai^x for ai in l]
        print(b)
        if sum(b) ==0:
            # print(x)
            return
    # return -1
    # print(6^6)

    # print(2^6)
    # print(5^6)
    # print(7^4^3)
    # print(3^6)




    
    # ---- CHECK FOR CORNER CASES ----
    
for _ in range(inp()):
    solve()