class Solution(object):
    def longestOnes(self, nums, k):
        l = 0
        zer = 0

        # n = len(nums)

        for r, n in enumerate(nums):
            if n == 0:
                zer += 1

            if zer > k:
                if nums[l] == 0:
                    zer -= 1
                l += 1

        return r - l + 1
