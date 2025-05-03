
i = int(input())
menuLine = []
for _ in range(i):
    l = list(map(int, input().split()))

    if l[0] == 1:
        menuLine.append(l[1])
    else:
        print(menuLine.pop(0))
