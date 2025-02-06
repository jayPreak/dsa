class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i, value in enumerate(nums):
            rem = target - nums[i]
            
            if rem in s:
                return [i, s[rem]]
            
            s[value] = i
                
                
                
        