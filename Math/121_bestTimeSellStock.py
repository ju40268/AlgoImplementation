class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # TLE approach
        # profit = 0
        # for i in range(len(prices) -1):
        #     for j in range(i, len(prices) -1):
        #         if prices[i] < prices[j+1]:
        #             diff = (prices[j+1] - prices[i])
        #             profit = max(profit, diff)
        # return profit
        
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit