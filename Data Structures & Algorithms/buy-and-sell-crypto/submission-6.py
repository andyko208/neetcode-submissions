class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # keep max_profit
        max_profit = 0
        # buy = 0
        buy = 0
        # iterate sell from 1 to n
        for sell in range(1, len(prices)):
            # get profit = prices[sell] - prices[buy]
            profit = prices[sell] - prices[buy]
            # update max_profit to max of current profit and itself
            max_profit = max(max_profit, profit)
            # update buy pointer if prices[sell] < prices[buy]
            if prices[sell] < prices[buy]:
                buy = sell
        # return max_profit
        return max_profit