class Solution:
    def canJump(self, nums: List[int]) -> bool:
        a = nums[0]
        for i in range(1, len(nums)):
            if a == 0:
                return False
            a -= 1

            a = max(a, nums[i])

        return True
        