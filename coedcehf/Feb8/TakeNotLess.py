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
    # print()
    n = inp()
    l = li()
    m = {}
    t =1
    

    l.sort(reverse=True)
    # print(l)
    for e in l:
        if e in m:
            m[e] += 1
        else:
            m[e] = 1
    
    # print(m.values())
    for key, value in m.items():
        if value%2:
            t = 0
            break

    if t:
        print("Zenyk")
    else:
        print("Marichka")
        

    # big = max(l)
    # # print(l.count(big))
    # if l.count(big) % 2!=0:
    #     print("Marichka")
    # else:
    #     print("Zenyk")



    # winner = "Marichka"
    # while len(l) != 1:
    #     big = max(l)
    #     if winner == "Marichka":
    #         l.remove(big)
    #         winner = "Zenyk"
    #     else:
    #         l.remove(big)
    #         winner = "Marichka"

    # print(winner)






    
    # ---- CHECK FOR CORNER CASES ----
    
for _ in range(inp()):
    solve()