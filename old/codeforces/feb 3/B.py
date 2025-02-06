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
    m = st()
    flag = False

    x, y = 0, 0
    # print(x, y)
    for i in m:
        if i == "U":
            y += 1
        elif i == "D":
            y -= 1
        elif i == "L":
            x -= 1
        elif i == "R":
            x += 1
        # print("x is", x)
        # print("y is", y)
        if x == 1 and y == 1:
            flag = True
            break
            
    
    if flag == True:
        print("YES")
    else:
        print("NO")

        





    
    # ---- CHECK FOR CORNER CASES ----
    
for _ in range(inp()):
    solve()