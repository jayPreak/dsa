import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
count = 0
Ω = []
for i in range(m):
    a, b = map(int, input().split())
    # print("a", a)
    # print("b", b)
    if a == b:
        continue
    if a > b:
        #swap 🤓
        a = a^b
        b = a^b
        a = a^b
    Ω.append((a,b))

seto = set(Ω)

count = m - len(seto)

# print(Ω)
print(count)

