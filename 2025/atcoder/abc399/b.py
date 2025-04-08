n = int(input())
l = list(map(int, input().split()))

    

for i in range(n):
    rank = 1
    for j in range(n):
        if l[j] > l[i]:
            rank +=1
    print(rank)