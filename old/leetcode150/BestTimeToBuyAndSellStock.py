# prices = [7, 1, 2, 3, 4, 6, 5]

# res = 0
# max = 0
# bought = False
# for i in range(len(prices)):
#     if bought:
#         if max < prices[i]:
#             max = prices[i]
#     else:
#         if max < prices[i]:
#             max = prices[i]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        max = 0
        min = prices[0]
        for price in prices:
            profit = price - min
            if profit > max:
                max = profit
            if price < min:
                min = price
        return max