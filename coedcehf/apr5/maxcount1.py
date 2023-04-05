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
# def solveS(s, m):
#    str_size = len(s)
#    count_0 = 0
#    count_1 = 0
#    for i in range(0, str_size - 1):
#       if (s[i] == '0'):
#          count_1 = 0
#          count_0 += 1
#       else :
#          count_0 = 0
#          count_1 += 1
#       if (count_0 == m or count_1 >0):
#          return True
#       count_1 = 0
#    return False


mod = 1000000007
INF = float("inf")

def solve():
    # print(1^1)
    n = inp()
    s = st()
    #count number of 1s in s
    # res = s.count('1')
    # flag = False
    # c0=0
    # c1=0
    # for i in range(0, len(s)):
    #     if s[i] == '0':
    #         c0+=1
    #         c1=0
    #     else:
    #         c1+=1
    #         c0=0
    #     if c0==2 and c1==0:
    #         flag = True
    #         break
    #     c1=0
    # # print(solveS(s, 2))
    # if flag:
    #     print(res+1)
    # else:
    #     print(res)

    # one0 = s[0]
    
    # zerosinline = 0

    # for i in range(1, len(s)):
    #     # print("zero?", one0)
    #     # print("curr", s[i])
    #     if one0 == "0":
    #         if s[i] == "0":
    #             zerosinline += 1
    #             one0 = "0"
    #         else:
    #             one0 = "1"
    #     else:
    #         if s[i] == "0":
    #             one0 = "0"
    #         else:
    #             one0 = "1"
        

    # # print(zerosinline)
    # if zerosinline == 0:
    #     print(res)
    # else:
    #     print(res + zerosinline)  
    # 
    # 
    # 
    # 

    zero = 0
    one = 1

    x = "1"
    y = "0"

    for i in range(1, len(s)):
        if x != s[i-1]:
            x = "1"
            one +=1
        else:
            x="0"
    for i in range(1, len(s)):
        if y!=s[i-1]:
            y="1"
            zero+=1
        else:
            y="0"

    print(max(zero, one))
    
     







    
    # ---- CHECK FOR CORNER CASES ----
    
for _ in range(inp()):
    solve()