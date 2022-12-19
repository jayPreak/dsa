from collections import Counter 
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))

    x = Counter(l)
    i = 0

    while True:
        if x[i] == 0:
            print("yes")
            break
        elif x[i] == 1:
            print("no")
            break
        i+=1

    

