class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        flag = False

        temp=set()

        for num in nums:
            if num in temp:
                flag = True
                break
            temp.add(num)
            
        return flag
        