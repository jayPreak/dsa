from re import L
import sys
import os.path
from math import *
from bisect import *
from itertools import *
from collections import defaultdict as dd, Counter
from itertools import accumulate
from operator import add
import math
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
    d = l.count(2)
    if (d%2==1):
        print(-1)
    else:
        c = 0
        for i in range(n):
            if(l[i]==2):
                c+=1
            if(c==(d//2)):
                break
        print(i+1)


    # print(6//2)


    # res = -1
    # left = 1
    # right = 1
    # # i = 0
    # for i in range(0, x):
    #     left *= l[i]
    #     # j = i+1
    #     for j in range(i+1, x):
    #         right *= l[j]
    #         # print("left is", left)
    #         # print("right is,", right)
    #     if left == right:
    #         res = i
    #         break
    #         # j+=1

    #     if res != -1:
    #         break
    #     right = 1
    #     # i+=1
    # if res == -1:
    #     print(res)
    # else:
    #     print(res+1)
    # l = x.copy()
    # m = {2: 0}
    # # t =1
    # res = -1

    # l.sort(reverse=True)
    # # print(l)
    # for e in l:
    #     if e in m:
    #         m[e] += 1
    #     else:
    #         m[e] = 1

    # # print(m)
    # # x = str(x)
    # # print(m.values()[0])
    # # print(m[2])
    # if m[2] !=0 and m[2]%2==0:
    #     res = [i for i, n in enumerate(x) if n == 2][1] +1
    #     # res = x
    # elif m[2] == 0:
    #     res = 1

    # print(res)

    # left = 1
    # right = 1

    # lp = 0
    # rp = -1

    # while True:
    #     if len(x)%2==0:
    #         if x.index(x[lp]) > x.index(x[rp]):
    #             print(-1)
    #             break
    #         else:
    #             left = left*x[lp]
    #             right = right*x[rp]
    #             if left == right:
    #                 print(lp+1)
    #                 break
    #             lp+=1
    #             rp-=1
    #     else:
    #         if x.index(x[lp]) == x.index(x[rp]):
    #             left = left*x[lp]
    #             if left == right:
    #                 print(lp+1)
    #                 break
    #         else:
    #             left = left*x[lp]
    #             right = right*x[rp]
    #             if left == right:
    #                 print(lp+1)
    #                 break
    #             lp+=1
    #             rp-=1

                
        








    
    # ---- CHECK FOR CORNER CASES ----
    
for _ in range(inp()):
    solve()