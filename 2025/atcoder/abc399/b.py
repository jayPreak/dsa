# list_c = [2,9,9,3]

# max_val = max(list_c)
# idx_max = list_c.index(max_val)

# print(max_val)
# print(idx_max)

# from re import L
import sys
import os.path
# from math import *
# from bisect import *
# from itertools import *
# from collections import defaultdict as dd, Counter
# from itertools import accumulate
# from operator import add
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
def simpleSplitListInp():
    return list(map(int, input().split()))


def printCleanList(x):
    print(*x, sep=" ")

def printListToStr(x):
    print(*x, sep="")

def printPretty2DList(x):
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in x]))


mod = 1000000007
# MAX_VAL = 10**6 

# arrayWithInt = [-1] * (MAX_VAL + 1) 
# empty2dArray = [[]] * (MAX_VAL + 1)

INF = float("inf")

def solve():
    n = inp()
    l = simpleSplitListInp()

    

    for i in range(n):
        rank = 1
        for j in range(n):
            if l[j] > l[i]:
                rank +=1
        print(rank)

    # # d = [0] * (100 + 1) 
    # # # print(d)
    # l = li()
    # r=1
    # ans = []

    # x = l.copy()
    # x.sort(reverse=True)
    # x = list(set(x))

    # for i in range(n):
    #     d[l[i]] += 1



    # for i in range(len(x)):

    #     # freq = l.count(x[i])
    #     # print(x[i])
    #     # print("l count", l.count(x[i]))
    #     toExtend = [r] * d[x[i]]
    #     ans.extend(toExtend)
    #     r+=d[x[i]]

    # print(ans)


    
solve()