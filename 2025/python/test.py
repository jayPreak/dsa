nums = [1,2,3,4]
flag = False
temp=set()

for num in nums:
    if num in temp:
        flag = True
        break
    temp.add(num)
    
print(flag)
    