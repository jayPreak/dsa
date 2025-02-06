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
    n, x = mp()
    z = st()
    # res = 0
    # # if x == 0:
    # #     res = int(z + "0")
    # # else:
    # for i in range(n+1):
    #         # print(z[:i], "ye[]")
    #         # print(z[:i] + str(x)+z[i::])
    #         m = int(z[:i] + str(x)+z[i::])
    #         res = max(res, m)

    # print(res)

    pos = n
    for i in range(n):
        if z[i] < str(x):
            pos = i
            break

    ans = z[:pos] + str(x) + z[pos:]
    print(ans)







    
    # ---- CHECK FOR CORNER CASES ----
    
for _ in range(inp()):
    solve()