A=list(map(int,input().split()))
L = []

for i in range(1,14):
        # print("i", i)
        # print("huh", A.count(i))
    L.append(A.count(i))


L.sort(reverse=True)

print("Yes" if L[0] >= 3 and L[1] >=2 else "No")