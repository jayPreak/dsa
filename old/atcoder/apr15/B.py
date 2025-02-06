from re import L
import sys
import os.path
from math import *
from bisect import *
from itertools import *
from collections import defaultdict as dd, Counter
from itertools import accumulate
from operator import add
# from sortedcontainers import SortedList as SL, SortedSet as SS, SortedDict as SD

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
    n = inp()
    a = []
    b = []
    res = False
    for i in range(n):
        a.append(li())
    for i in range(n):
        b.append(li())
    for _ in range(4):
        if all(a[i][j] == 0 or b[i][j] == 1 for i in range(len(a)) for j in range(len(a))):
            res = True
        a = [[a[len(a) - j - 1][i] for j in range(len(a))]
             for i in range(len(a))]
    print("YES" if res else "NO")

    # ---- CHECK FOR CORNER CASES ----


solve()
