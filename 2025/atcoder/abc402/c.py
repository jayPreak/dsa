
n, m = map(int, input().split())
days = [0] * n
foods = []

for _ in range(m):
    l = list(map(int, input().rstrip().split()))
    foods.append(l)

orders = [0] * (n+1)

z = list(map(int, input().rstrip().split()))
for i in range(len(z)):
    orders[z[i]] = i+1
# print("no dislike", z)
for i in range(len(foods)):
    maxToEat = 0
    for j in range(1, len(foods[i])):
        maxToEat = max(orders[foods[i][j]], maxToEat)
    days[maxToEat-1] += 1

temp = 0
for i in days:
    temp += i
    print("%d\n"%temp)