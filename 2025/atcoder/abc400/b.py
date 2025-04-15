n, m = map(int, input().split())
inf = 10 ** 9
res = 1

for i in range(0, m):
    res += n ** (i+1)

if res <= inf:
    print(res)
else:
    print("inf")