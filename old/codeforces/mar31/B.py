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
    n = inp()
    # print(n, "yeppp")
    candies = 1
    res = 0
    resli = []
    if n % 2 ==0:
        print(-1)
    else:
        i = 0
        while i <= 40:
            i+=1
            if (2*candies)+1 == n:
                res = i
                resli.append(2)
                break
            elif (2*candies)-1==n:
                res = i
                resli.append(1)
                break
            else:
                if (2*candies)+1 < n:
                    candies = (2*candies)+1
                    resli.append(2)
                    if candies == n:
                        res=i
                        break
                elif (2*candies)+1 > n:
                    candies = (2*candies)-1
                    resli.append(1)
                    if candies == n:
                        res=i
                        break
                

        print(res)
        printCleanList(resli)



        






    
    # ---- CHECK FOR CORNER CASES ----
    
for _ in range(inp()):
    solve()