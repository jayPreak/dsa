class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        n = len(candies)

        def largest(arr, n):
            max = arr[0]
            for i in range(1, n):
                if arr[i] > max:
                    max = arr[i]
            return max

        max = largest(candies, n)
        print(max)
        for i in range(n):
            print('sum is,', candies[i] + extraCandies)
            print('res is', res)
            if candies[i] + extraCandies >= max:
                res.append(True)
            else:
                res.append(False)

        return res
