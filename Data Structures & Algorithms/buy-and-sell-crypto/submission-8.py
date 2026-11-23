class Solution: 
    def maxProfit(self, prices: List[int]) -> int:
        # Time: O(n) from iteration
        # Space: O(1)
        # keep a buy pointer
        buy = prices[0]
        profit = 0
        # iterate through prices
        for p in prices[1:]:
            # if prices[i] < buy, update buy
            # profit = max(profit, sell-buy)
            profit = max(profit, p-buy)
            if p < buy:
                buy = p
        return profit