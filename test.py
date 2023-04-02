def solve(n, a):
    for x in range(28):
        b = [ai ^ x for ai in a]
        if sum(b) == 0:
            return x
    return -1

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
