class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # res = False
        # j = 0
        # if len(nums) < 3:
        #     return res
        # for i in range(len(nums)):
        #     temp = []
        #     temp.append(nums[i])
        #     j = i+1
        #     while j < len(nums):
        #         if nums[j] > temp[-1]:
        #             temp.append(nums[j])
        #         if nums[j] > temp[0]:
        #             temp.pop(-1)
        #             temp.append(nums[j])
        #         if len(temp) == 3:
        #             return True
        #         j += 1
        # return False

        first = second = math.inf

        for i in nums:
            if i <= first:
                first = i
            elif i <= second:
                second = i
            else:
                return True
        return False
