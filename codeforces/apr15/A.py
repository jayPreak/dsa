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
    # print()
    s = st()
    count = 0
    i = 0
    while i < len(s):
        if s[i] == "^":
            if i + 2 < len(s) and s[i + 1] == "_" and s[i + 2] == "^":
                i += 3
            elif i + 1 < len(s) and s[i + 1] == "^":
                i += 2
            else:
                count += 1
                i += 1
        else:
            if i == 0 or i == len(s) - 1 or (s[i - 1] != "^" and s[i + 1] != "^"):
                count += 1
            i += 1
    print(count)

    # ---- CHECK FOR CORNER CASES ----
for _ in range(inp()):
    solve()
