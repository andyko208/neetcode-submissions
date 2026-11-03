class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # # define a recursive function that takes in amount
        # dp = [0] * (amount + 1)
        # def dfs(total):
        #     # base case to return 0 if amount == 0
        #     if total <= 0:
        #         return 0 if total == 0 else float('inf')
        #     # memoization
        #     # print(total)
        #     if dp[total] != 0:
        #         return dp[total]
        #     res = float('inf')
        #     # iterate through c in coins
        #     for c in coins:
        #         # res = min(res, 1 + dfs(amount-c))
        #         res = min(res, 1 + dfs(total - c))
        #     # update dp at amount to res
        #     dp[total] = res
        #     # return dp at amount
        #     return dp[total]
        # minCoins = dfs(amount)
        # return minCoins if minCoins != float('inf') else -1

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

