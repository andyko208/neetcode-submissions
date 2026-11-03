class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Time: O(n*amount), Space: O(amount)
        # define a dp list of size amount + 1
        dp = [float('inf')] * (amount + 1)
        # base case: set dp[0] to 0
        dp[0] = 0
        # iterate through 1 to amount
        for a in range(1, amount+1):
            # iterate through c in coins
            for c in coins:
                # update dp[i] to min of dp[i] and 1 + dp[amount-c]
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
        # return dp[amount] if dp[amount] != float('inf') else -1
        return dp[amount] if dp[amount] != float('inf') else -1

