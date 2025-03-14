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
INF = float("inf")

def solve():
    n = inp()
    arr = [["?"] * n for _ in range(n)]
    # print(arr)

    for i in range(n):
        j = n-i-1
        # print("i", i)
        # print("j", j)
        for a in range(i, j+1):
            for b in range(i, j+1):
                # print("a", a)
                # print("b", b)
                if i % 2 == 0:
                    arr[a][b] = "#"
                else:
                    arr[a][b] = "."

                # printPretty2DList(arr)

    for row in arr:
        print("".join(row))


    
solve()