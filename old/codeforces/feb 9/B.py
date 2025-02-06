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

def sum(n):
    sum = 0
    while n>0:
        sum+=n%10
        n /= 10
    return sum

def solve():
    # print()
    n = inp()
    x = int(n/2)
    y = n -x
    sum1 = sum(x)
    sum2 = sum(y)
    # print(sum1, sum2)
    if abs(sum1 - sum2)>1:
        if sum1 < sum2:
            x -= 1
        else:
            y -= 1
    print(x, y)
    





    
    # ---- CHECK FOR CORNER CASES ----
    
for _ in range(inp()):
    solve()