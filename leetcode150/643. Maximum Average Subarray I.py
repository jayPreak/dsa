class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxi = sum(nums[:k])
        curr = sum(nums[:k])
        # i = 0
        # while i < len(nums):
        #     sum = 0
        #     if i + k <= len(nums):

        #         for j in range(i, i+k):
        #             sum += nums[j]

        #     maxi = max(maxi, sum/k)
        #     i+=1
        # return maxi

        for i in range(k, len(nums)):
            curr += nums[i] - nums[i-k]
            maxi = max(maxi, curr)

        return maxi/k
