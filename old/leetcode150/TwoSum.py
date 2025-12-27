class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i, value in enumerate(nums):
            rem = target - nums[i]
            
            if rem in s:
                return [i, s[rem]]
            
            s[value] = i
                
                
                
  class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
               