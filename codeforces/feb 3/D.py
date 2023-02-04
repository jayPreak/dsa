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
    # a = dict.fromkeys(s,0)
    # b = dict.fromkeys(s,0)
    # # print(a)
    # b1 = [0] * n
    # b2 = [0] * n


    # b1[0] = 1
    # a[s[0]] += 1
    # # print()
    # # print(a)
    # for i in range(1, n):
    #     if s[i] == s[-1]:
    #         b1[i] = 1 + b1[i-1]
    #     else:
    #         b1[i] = b1[i-1]

    #     a[s[i]] += 1


    # b2[n-1] = 1
    # b[s[n-1]] += 1
    # for i in range(n-2, 0):
    #     if s[i] == s[-1]:
    #         b2[i] = 1 + b2[i+1]
    #     else:
    #         b2[i] = b2[i+1]
        
    #     b[s[i]] += 1


    # ans = 0
    # for i in range(n):
    #     ans = max(ans, b1[i] + b2[i])

    # if(ans>n):
    #     ans = n

    # print(ans)
    # a = dict.fromkeys(s,0)

    # for i in range(n):
    #     a[s[i]]+=1

    # ans = 0
    # for i in range(0, len(a)):
    #     print(a.items(0))
    # for key, value in a.items:
    #     ans = max(ans, value)

    # print(min(n - ans + 1, ans))
    m = dict()
    for i in range(n):
        if s[i] not in m:
            m[s[i]] = 1
        else:
            m[s[i]] += 1

    ans = 0

    for i in m:
        ans = max(ans, m[i])

    print(min(n - ans + 1, ans))




    
    # ---- CHECK FOR CORNER CASES ----
    
for _ in range(inp()):
    solve()




