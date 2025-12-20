# import sys

# nums = [1 , 1, 2]

# m = list(set(nums))

# m.sort()

# for i in range(len(m)):
#     nums[i] = m[i]

# print(nums)
#my 3yo solution 😭
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         m = list(set(nums))
#         m.sort()
#         for i in range(len(m)):
#             nums[i] = m[i]
            
#         return len(m)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            # print(i)
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j
        