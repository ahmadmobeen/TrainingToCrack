class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
  
        buy = 0
        sell = 0
        max_profit = 0
        profit = 0
        buy = prices[0]
        i = 0
        while i < len(prices):
            
            sell = prices[i] # move sell price to next day
            if buy > sell:
                buy = sell   # if encounter a cheaper price, move the buy day to the cheap day
            else:
                profit = sell - buy
            if profit > max_profit:
                max_profit = profit
            i += 1
        return max_profit
            
            
            
            
#         max_profit = 0 #### exceeds time complexity
#         for i in range(len(prices)):
            
#             for j in range(i+1, len(prices)):
#                 if prices[j] - prices[i] > max_profit:
#                     max_profit = prices[j] - prices[i]
#         if len(prices) > 1:
#             return max_profit if max_profit > 0 else 0
#             # return max(profit) if max(profit) > 0 else  0
#         return 0
