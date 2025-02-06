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
    n = inp()
    s = st()
    
    # print(s[1:-1])
    # while True:
    #     if len(s) < 3:
    #         break
    while len(s)>2:
        if (s[0] == "1" and s[-1] == "0") or (s[0] == "0" and s[-1] == "1"):
            s = s[1:-1]
        else:
            break
        
    if len(s) > 2:
        print(len(s))
    elif len(s) == 2:
        if s == "10" or s == "01":
            print(0)
        else:
            print(2)
    else:
        print(1)





    
    # ---- CHECK FOR CORNER CASES ----
    
for _ in range(inp()):
    solve()