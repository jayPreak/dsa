class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, l, prefix = 0, 0, 0
        for r, n in enumerate(nums):
            prefix += n
            while prefix < r-l:
                prefix -= nums[l]
                l += 1
            res = max(res, r-l)
        return res
