n = int(input())



if n % 2 == 0:
    ans = "-" * (n-2)
    sliceIdx = (n//2)-1
    ans = ans[:sliceIdx] + "==" + ans[sliceIdx:]
    

else:
    ans = "-" * (n-1)
    sliceIdx = (n//2)
    ans = ans[:sliceIdx] + "=" + ans[sliceIdx:]

print(ans)


