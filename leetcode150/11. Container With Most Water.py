class Solution:
    def maxArea(self, height: List[int]) -> int:
        # def maxI(arr):
        #     max = arr[0]
        #     for i in arr:
        #         if i > max:
        #             max = i

        #     return max

        # first = maxI(height)
        # height.remove(first)
        # second = maxI(height)
        left = 0
        right = len(height) - 1
        vol = 0

        while left < right:
            width = right - left
            hieght = min(height[left], height[right])
            area = width * hieght

            vol = max(vol, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return vol
