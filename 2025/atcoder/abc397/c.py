n=int(input())
a=list(map(int,input().split()))
left=[0]*n
right=[0]*n
leftnum=0
rightnum=0

for i in a:
    
    right[i-1]+=1

for i in right:
    if i!=0:
        rightnum+=1

maxnum=rightnum

for i in range(1,n):
    
    left[a[i-1]-1]+=1
    print("a", a[i-1]-1)
    print(left[a[i-1]-1])
    if left[a[i-1]-1]==1:
        leftnum+=1

print(leftnum)

print(left)