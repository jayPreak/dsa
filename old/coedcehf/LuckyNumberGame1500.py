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

mod = 1000000007
INF = float("inf")

def solve():
    # print("ye")
    n, b, a = mp()
    x = li()
    BOB = 0
    ALICE = 0
    c = 0
    
    for i in x:
        if i%b == 0 and i%a == 0:
            c += 1
        elif i%b == 0 and i%a != 0:
            BOB +=1
        elif i%b !=0 and i%a == 0:
            ALICE +=1

    if c > 0 and BOB >= ALICE:
        print("BOB")
    elif c > 0 and BOB < ALICE:
        print("ALICE")
    elif c == 0:
        if BOB > ALICE:
            print("BOB")
        else:
            print("ALICE")





    
    # ---- CHECK FOR CORNER CASES ----
    
for _ in range(inp()):
    solve()