k =3
nums = [1,2,3,4,5,6,7]
temp = []

nums = nums[-k:] + nums[:-k]


for i in range(k):
    nums.insert(0, nums.pop(-1))
    
print(nums)
    