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

mod = 1000000007
INF = float("inf")

def solve():
    pi = "3141592653589793238462643383279"
    x = st()
    # print(x[0:2])
    for i in range(len(x)+1):
        if i == 0:
            if x[0] == pi[0]:
                res = 1
            else:
                res = 0
        elif i > 0 and x[0:i] == pi[0:i]:
            res = i
            # print(res, " and i is: ", i, " and x{0:4} is", x[0:i], "pi is ", pi[0:i])
        

    print(res)





    
    # ---- CHECK FOR CORNER CASES ----
    
for _ in range(inp()):
    solve()