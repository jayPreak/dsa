class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxfar = nums[0]
        currmax = nums[0]

        for i in range(1, len(nums)):
            currmax = max(nums[i], currmax + nums[i])
            maxfar = max(maxfar, currmax)

        return maxfar