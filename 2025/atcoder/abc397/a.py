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
    
def normalListInp():
    return list(input())
def normalStringArrayInput():
    return input().split(" ")
    
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
    x = float(input())

    if (x >= 38.0):
        print(1)
    elif (38.0 > x>= 37.5):
        print(2)
    else:
        print(3)





    
    


    

    
solve()