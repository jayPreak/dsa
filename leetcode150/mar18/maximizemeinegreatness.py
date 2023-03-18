class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        count = [0] * 101
        for num in nums:
            count[num] += 1
        
        greatness = 0
        perm_idx = 0
        for num in reversed(range(101)):
            if count[num] == 0:
                continue
            greatness += min(perm_idx, count[num])
            perm_idx += count[num]
        
        return greatness