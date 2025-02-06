class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        def mulList(lst):
            result = 1
            for x in lst:
                if x != 0:
                    result *= x
            return result
        res = []

        proded = mulList(nums)
        # print(proded)
        haszero = False
        zeroes = nums.count(0)
        if zeroes > 0:
            haszero = True

        for i in range(len(nums)):
            if haszero:
                if nums[i] == 0:
                    if zeroes == 1:
                        res.append(proded)
                    else:
                        res.append(0)
                else:
                    res.append(0)
            else:
                res.append(proded//nums[i])

        print(res)
        return res
