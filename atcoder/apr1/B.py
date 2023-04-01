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
    # n = inp()
    s1 = st()
    s2 = st()
    s3 = st()
    s4 = st()
    s5 = st()
    s6 = st()
    s7 = st()
    s8 = st()
    res = ""

    y = ord("a")

    if "*" in s1:
        pos = s1.index("*")
        alph = y + pos
        res = chr(alph) + "8"
        print(res)
    if "*" in s2:
        pos = s2.index("*")
        alph = y + pos
        res = chr(alph) + "7"
        print(res)
    if "*" in s3:
        pos = s3.index("*")
        alph = y + pos
        res = chr(alph) + "6"
        print(res)
    if "*" in s4:
        pos = s4.index("*")
        alph = y + pos
        res = chr(alph) + "5"
        print(res)
    if "*" in s5:
        pos = s5.index("*")
        alph = y + pos
        res = chr(alph) + "4"
        print(res)
    if "*" in s6:
        pos = s6.index("*")
        alph = y + pos
        res = chr(alph) + "3"
        print(res)
    if "*" in s7:
        pos = s7.index("*")
        alph = y + pos
        res = chr(alph) + "2"
        print(res)
    if "*" in s8:
        pos = s8.index("*")
        alph = y + pos
        res = chr(alph) + "1"
        print(res)
        


    
    







    
    # ---- CHECK FOR CORNER CASES ----
    
solve()