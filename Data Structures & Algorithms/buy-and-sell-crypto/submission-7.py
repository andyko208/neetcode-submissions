class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time: O(n) from iterating through prices
        # Space: O(1)
        # edge case
        if len(prices) == 1:
            return 0
        # keep two pointers for buy and sell
        n = len(prices)
        buy = prices[0]
        profit = 0
        # move up the sell pointer to maximize the profit
        for i in range(1, n):
            sell = prices[i]
            # maximize the profit
            profit = max(profit, sell - buy)
            # update buy pointer to sell if it's smaller
            buy = min(buy, sell)
        return profit
# edge case
# [2, 1]