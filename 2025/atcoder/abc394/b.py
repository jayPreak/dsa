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
    # res = st()

    # for _ in range(n-1):
    #     s = st()
    #     if len(res) > len(s):
    #         res = s + res
    #     else:
    #         res = res + s
    # print(res)
    #brutey wrutey
    print(n)
    arr = []
    for _ in range (n):
        s = st()
        # print(s)
        arr.append(s)

    
    res =sorted(arr, key=len)
    printListToStr(res)



        
    

        


    
solve()