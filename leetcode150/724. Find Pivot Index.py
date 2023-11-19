class Solution(object):
    def pivotIndex(self, nums):
        # """
        # :type nums: List[int]
        # :rtype: int
        # """
        # i = len(nums)//2
        # l = r = i
        # print(l)
        # if len(nums)<4:
        #     print(sum(nums[1:-1]))
        # while -1 < l and r  < len(nums)+1:
        #     if sum(nums[0:l]) == sum(nums[l:-1]):
        #         print('left left sum', sum(nums[0:l]))
        #         print('left rightsum', sum(nums[l:-1]))
        #         return l
        #     if sum(nums[0:r]) == sum(nums[r:-1]):
        #         print('right left sum', sum(nums[0:r]))
        #         print('right rightsum', sum(nums[r:-1]))
        #         return r
        #     l -= 1
        #     r += 1
        # return -1

        l = 0
        r = sum(nums)

        for i, curr in enumerate(nums):
            r -= curr
            if l == r:
                return i
            l += curr

        return -1
