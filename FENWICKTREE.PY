def getsum(btree, i):
    s = 0
    i = i+1
    while i>0:
        s += btree[i]

        i -= i & (-i)

    return s

def updatebit(btree, n, i, v):
    i += 1
    while i <= n:
        btree[i] += v
        i += i & (-i)

def construct(arr, n):
    btree = [0] * (n+1)

    for i in range(n):
        updatebit(btree, n, i, arr[i])

    return btree

if __name__ == "__main__":
    freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    btree = construct(freq, len(freq))
    print("sum of elements from 0 to 5is ", getsum(btree,5))
    freq[3] += 6
    updatebit(btree, len(freq), 3, 6)
    print("sum of elements from 0 to 5 agteer update ", getsum(btree, 5))
    
