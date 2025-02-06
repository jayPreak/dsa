for _ in range(int(input())):
    n = int(input())
    f = lambda : map(str, input().split())
    h = {}
    for j in range(3):
        for i in range(n):
            a, b = f()
            b = int(b)
            if a in h:
                h[a] += b
            else:
                h[a] = b

    print(h)

    sorredh = sorted(h.items(), key = lambda x: x[1])
    result = []
    for i in range(len(sorredh)):
        result.append(sorredh[i][1])

    print(*result, sep = " ")
