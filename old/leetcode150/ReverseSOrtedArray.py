#slower cuz not in is like O(n) XD

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if target not in nums:
#             return -1
#         else:
#             return nums.index(target)



class Solution(object):
    def search(self, nums, target):
        if (not nums):
            return -1

        pivotindex = self.findpivot(nums)
        res = self.binarys(nums, target, 0, pivotindex-1)
        if res != -1:
            return res
        else:
            return self.binarys(nums, target, pivotindex, len(nums)-1)

        
    def findpivot(self, arr):
        elem = arr[-1]
        low = 0
        high = len(arr)-1
        while (low<=high):
            mid = (low+high)//2
            if elem < arr[mid]:
                low = mid + 1
            elif elem >= arr[mid]:
                high = mid - 1

        return low
        
    def binarys(self, arr, value, low, high):
        while (low<=high):
            mid = (low+high)//2
            if value < arr[mid]:
                high = mid - 1
            elif value > arr[mid]:
                low = low + 1
            else:
                return mid
        return -1
        

#fk this man
