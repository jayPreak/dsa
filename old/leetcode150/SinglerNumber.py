# from collections import Counter
 
# # initializing string
# test_str = [1, 2, 3, 4, 5, 6, 1]
 
# # using collections.Counter() to get
# # count of each element in string
# res = Counter(test_str)
# z = res.most_common()
# print(z[-1][0])

# from collections import Counter

# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         a = Counter(nums)
#         b = a.most_common()
#         return b[-1][0]


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = {}
        for num in nums:
            if num not in x:
                x[num] = 1
            else:
                x[num] += 1
                
        for key, val in x.items():
            if val == 1:
                return key
        