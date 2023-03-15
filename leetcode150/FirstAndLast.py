class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(x):
            low = 0
            hi = len(nums)
            while low < hi:
                mid = (low+hi)//2
                if nums[mid] < x:
                    low = mid+1
                else:
                    hi = mid
            return low

        low = search(target)
        high = search(target+1) -1

        if low <=high:
            return [low, high]
        else:
            return[-1, -1]

                
