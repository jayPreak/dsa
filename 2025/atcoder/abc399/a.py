n = int(input())
s = list(input())
y = list(input())
count = 0

for i in range(n):
    if s[i] != y[i]:
        count +=1

print(count)