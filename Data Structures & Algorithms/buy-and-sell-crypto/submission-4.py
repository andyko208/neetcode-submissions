class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute force with 2 iteration of loops
        n = len(prices)
        profit = 0
        # iterate i from 0 to n-1
        for i in range(n):
            # iterate j from i+1 to n
            for j in range(i+1, n):
                # update max by max(prices[i] - prices[j])
                profit = max(profit, prices[j] - prices[i])
        return profit