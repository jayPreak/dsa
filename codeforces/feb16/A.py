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

def checkBeau(a):
    i = 0
    j = 1
    beau1 = True
    while True:
        if i == len(a) - 1:
            break
        if a[i] == a[j]:
            beau1 = False
            # print(a[i], "yes")
            break
        i+=1
        j+=1
    return beau1

mod = 1000000007
INF = float("inf")

def solve():
    # print()
    n, m = mp()
    a = st()
    b = st()

    x = a+b[::-1]

    if ("RRR" in x) or ("BBB" in x) or (x.count("RR")+x.count("BB") > 1):
        print("NO")
    else:
        print("YES")




    

    







    
    # ---- CHECK FOR CORNER CASES ----
    
for _ in range(inp()):
    solve()