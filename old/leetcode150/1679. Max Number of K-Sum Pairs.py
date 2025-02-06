class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1
        count = 0

        while left < right:
            print('left', nums[left])
            print('right', nums[right])

            if nums[left]+nums[right] == k:
                count += 1
                left += 1
                right -= 1
            elif nums[left]+nums[right] < k:
                # print('hii', nums.pop(left))
                left += 1
            else:
                right -= 1

        return count
