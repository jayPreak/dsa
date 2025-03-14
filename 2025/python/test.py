nums = [4,1,2,1,2]
hash = {}
 
for num in nums:
    
    if num in hash:
        hash[num] += 1
    else:
        hash[num] = 1
        
for key in hash:
    if hash[key] == 1:
        print(key)
        break
     