class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # count = 0
        # i = 0

        # while i < len(nums):
        #     if nums[i] == 0:
        #         nums.pop (i)
        #         count += 1
        #     else:
        #         i+=1

        # while count != 0:
        #     nums.append(0)
        #     count -= 1

        i = 0
        for x in nums:
            if x != 0:
                nums[i] = x
                i += 1

        for z in range(i, len(nums)):
            nums[z] = 0
