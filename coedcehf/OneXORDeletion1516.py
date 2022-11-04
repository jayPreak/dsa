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
    s = set(l)
    s = list(s)
    for i in range(0, n, 2):
        ans = min(ans, n - f[s[i]] - f[s[i+1]])

    
    print(f)
    print("yep", f[s[0]])

