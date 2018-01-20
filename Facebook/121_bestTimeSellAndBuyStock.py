class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        
        min_val, profit = prices[0], 0
        
        for p in prices:
            min_val = min(min_val, p)
            profit = max(profit, p - min_val)
        
        return profit