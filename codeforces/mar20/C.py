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
    s = st()

    evens = set()
    odds = set()

    for i in range(len(s)):
        if i%2==0:
            if s[i] in odds:
                print("NO")
                return
            evens.add(s[i])
        else:
            if s[i] in evens:
                print("NO")
                return
            odds.add(s[i])
    # else:
    print("YES")






    
    # ---- CHECK FOR CORNER CASES ----
    
for _ in range(inp()):
    solve()