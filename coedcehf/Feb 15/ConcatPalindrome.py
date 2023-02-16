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
    # print()
    n, m = mp()
    a = st()
    b = st()
    if len(a) < len(b):
        a, b = b, a

    d1 = {}
    for i in a:
        if i not in d1:
            d1[i] = 1
        else:
            d1[i] += 1

    ans = True
    

    for i in b:
        if d1.get(i) is not None and d1[i]>0:
            d1[i] -= 1
        else:
            ans = False
            break
    # print(d1)

    o = 1
    for key, value in d1.items():
        if value%2 == 1:
            if o:
                o = 0
            else:
                ans = False
        else:
            pass

    if ans:
        print("yes")
    else:
        print("no")
    








    
    # ---- CHECK FOR CORNER CASES ----
    
for _ in range(inp()):
    solve()