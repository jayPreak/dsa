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
    x = inp()
    s = st()

    m = ['m', 'M']
    e = ['e', 'E']
    o = ['o', 'O']
    w = ['w', 'W']

    all = ['m', 'M', 'e', 'E', 'o', 'O', 'w', 'W']
    cat = False
    mfound = False
    efound = False
    ofound = False
    wfound = False

    for i in range(len(s)):
        if wfound:
            if s[i] in w:
                # print('hiiw?')
                cat = True
            elif s[i] in m:
                cat = False
                break
            else:
                cat = False
        elif ofound:
            if s[i] in o:
                ofound = True
            elif s[i] in w:
                # print("yo?")
                wfound = True
                cat = True
            else:
                cat = False
                break
        elif efound:
            if s[i] in e:
                efound = True
            elif s[i] in o:
                ofound = True
            else:
                cat = False
                break
        elif mfound:
            if s[i] in m:
                # print("mfound" + s[i])
                mfound = True
            elif s[i] in e:
                # print('efound' + s[i])
                efound = True
            else:
                cat = False
                break
        else:
            if s[i] in m:
                # print("yes")
                mfound = True
                # print("um?")
            else:
                cat = False
                break

    # for i in range(len(s)):
    #     if i == len(s) - 1:
    #         # print('yes')
    #         if ofound == True:
    #             if s[i] in w:
    #                 cat = True
    #                 break
    #     else:
    #         if cat == False:
    #             if ofound:
    #                 if s[i] in o:
    #                     ofound = True
    #                 if s[i] in w:
    #                     cat = True
    #                     break
    #             elif efound:
    #                 if s[i] in e:
    #                     efound = True
    #                 if s[i] in o:
    #                     ofound = True
    #             elif mfound:
    #                 if s[i] in m:
    #                     mfound = True
    #                 if s[i] in e:
    #                     efound = True
    #             else:
    #                 if s[i] in m:
    #                     mfound = True


    # for i in s:
    #     if i not in all:
    #         cat = False
    
    if cat:
        print('YES')
    else:
        print('NO')


                









    
    # ---- CHECK FOR CORNER CASES ----
    
for _ in range(inp()):
    solve()