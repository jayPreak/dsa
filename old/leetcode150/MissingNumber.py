class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            if 1 not in nums:
                return 1
            else:
                return 0
        else:
            res = 0
            for i in range(len(nums)):
                if i+1 not in nums:
                    return i+1
                else:
                    res = 0

        return res