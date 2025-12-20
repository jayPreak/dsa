class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
                
        return profit

# well i got worse
#  class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         res = []
#         for i in range(0, len(prices)-1):
#             if prices[i] < prices[i+1]:
#                 res.append(prices[i+1] - prices[i])

#         return sum(res)
                
               