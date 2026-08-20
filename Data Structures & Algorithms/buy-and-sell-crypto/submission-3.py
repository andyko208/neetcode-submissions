class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we want to be keep finding max profit
        profit = 0
        buy = 0
        n = len(prices)
        # keep incrementing when to sell while preserving max profit
        for sell in range(1, n):
            profit = max(profit, prices[sell] - prices[buy])
            # find a better buy each iter
            if prices[sell] < prices[buy]:
                buy = sell
        return profit