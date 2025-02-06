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
    s = st()
    distinct_colors = len(set(s))
    color_counts = {color: s.count(color) for color in set(s)}
    if distinct_colors == 4 or (distinct_colors == 2 and all(count == 2 for count in color_counts.values())):
        # It is possible to turn all bulbs on
        turns = 0
        while '0' in s:
            distinct_colors = set(s)
            for color in distinct_colors:
                if color != '0' and (s.count(color) > 1 or '0' in s.replace(color, '')):
                    s = s.replace(color, '1')
            turns += 1
            s = s.replace('0', '1', 1)
        print(turns)
    else:
        # It is impossible to turn all bulbs on
        print(-1)







    
    # ---- CHECK FOR CORNER CASES ----
    
for _ in range(inp()):
    solve()