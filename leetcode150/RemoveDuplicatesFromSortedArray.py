# import sys

# nums = [1 , 1, 2]

# m = list(set(nums))

# m.sort()

# for i in range(len(m)):
#     nums[i] = m[i]

# print(nums)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        m = list(set(nums))
        m.sort()
        for i in range(len(m)):
            nums[i] = m[i]
            
        return len(m)
        