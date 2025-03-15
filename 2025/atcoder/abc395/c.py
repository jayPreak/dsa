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

def printPretty2DList(x):
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in x]))


mod = 1000000007
MAX_VAL = 10**6 
arrayWithInt = [-1] * (MAX_VAL + 1) 
empty2dArray = [[]] * (MAX_VAL + 1)

INF = float("inf")

def solve():
    n = inp()
    l = li()

    minValue = float('inf')
    # print(min)

    for i, v in enumerate(l):
        # print("minValue", minValue)
        # print(arrayWithInt)
        if arrayWithInt[v] != -1:
            minValue = min(minValue, i - arrayWithInt[v] +1)

        

        arrayWithInt[v] = i

    print(minValue if minValue != float('inf') else -1)


    #brute force 😈
    # print(l)
    # current = l[0]
    # start = 0

    # if n == 1:
    #     print(1)
    #     return

    # while start < n:
    #     # print("start", start)
    #     for i in range(start+1, n):
    #         # print("current", current)
    #         if current == l[i]:
    #             print(i+1)
    #             return
    #     start +=1
    #     if start < n:
    #         current = l[start]
        
    # print(-1)


        
    

        


    
solve()