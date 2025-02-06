import collections

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    
    # i = 0
    # count = 0
    # while i <len(l)-1:
    #     if l[i] == l[i+1]:
    #         i+=2
    #     elif l[i]%2==0 and l[i+1] == l[i]+1:
    #         i+=2
    #     else:
    #         count+=1
    #         i+=2

    # print(count)

    f = collections.Counter(l)
    f = dict(f)

    ans = n
    for x in l:
        ans = min(ans, n - f[x])
        if x%2==0:
            if (x+1) not in f:
                f[x+1] = 0
            ans = min(ans, n - (f[x] + f[x+1]))

    print(ans)

    
    # print(f)
    # print("yep", f[s[0]])

