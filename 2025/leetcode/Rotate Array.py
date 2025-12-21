# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         for i in range(k):
#             nums.insert(0, nums.pop(-1))


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            x = nums.pop()
            nums.insert(0, x)
        