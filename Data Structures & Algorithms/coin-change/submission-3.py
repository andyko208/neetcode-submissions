class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # cache a dp list filled with amount + 1 of size amount + 1
        dp = [amount + 1] * (amount + 1)
        # initialize dp[0] to be 0(no steps needed to reach from 0 to 0)
        dp[0] = 0
        # iterate i from 1 to amount
        for i in range(1, amount + 1):
            # iterate c in coins
            for c in coins:
                # dp[i] = min(dp[i], 1 + dp[i - c])
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - c])
            # return dp[amount] if != amount + 1
        minAmount = dp[amount]
        return minAmount if minAmount != amount + 1 else -1

