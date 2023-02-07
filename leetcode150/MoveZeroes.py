# nums = [1, 0, 2, 3, 1, 0, 4]
# print(nums)
# one = [x for x in nums if x !=0]
# two = [j for j in nums if j == 0]
# nums =  one + two 
# print(nums)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for x in nums:
            if x != 0:
                nums[i] = x
                i+=1

        for z in range(i, len(nums)):
            nums[z] = 0