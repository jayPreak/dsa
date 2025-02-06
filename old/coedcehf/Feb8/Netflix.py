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
    a, b, c, x = mp()
    # print(a, b, c, x)
    if a + b > x or a+b==x:
        print("YES")
    elif b + c > x or b+c==x:
        print("YES")
    elif a + c > x or a+c==x:
        print("YES")
    elif a > x or b > x or c > x or a==x or b ==x or c==x:
        print("YES")
    else:
        print("NO")




    
    # ---- CHECK FOR CORNER CASES ----
    
for _ in range(inp()):
    solve()