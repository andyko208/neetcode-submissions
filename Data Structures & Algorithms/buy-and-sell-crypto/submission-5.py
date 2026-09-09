class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # # Brute force with 2 iteration of loops
        # n = len(prices)
        # profit = 0
        # # iterate i from 0 to n-1
        # for i in range(n):
        #     # iterate j from i+1 to n
        #     for j in range(i+1, n):
        #         # update max by max(prices[i] - prices[j])
        #         profit = max(profit, prices[j] - prices[i])
        # return profit
        # Optimized sliding window approach
        # keep a pointer buy at 0 and sell at 0
        l = 0
        # update profit by maximizing sell - buy
        profit = 0
        # iterate r from 1 to n
        for r in range(len(prices)):
            # if buy < sell, buy = sell
            buy, sell = prices[l], prices[r]
            profit = max(profit, sell - buy)
            if sell < buy:
                l = r
        return profit