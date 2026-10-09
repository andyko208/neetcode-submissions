class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # recursive call to use all
        # dp list to len amount + 1 of val amount
        dp = [float('inf')] * (amount + 1)
        memo = {}

        # define dfs that takes in amount
        def dfs(amount):
            # base case to return 0 if amount == 0
            if amount == 0:
                return 0
            # base case to return dp[amount]
            if amount in memo:
                return memo[amount]
            # iterate through c in coins
            res = float('inf')
            for c in coins:
                # if amount - c >= 0, dp[i] = min(dp[i], 1 + dfs(amount-c))
                if amount - c >= 0:
                    res = min(res, 1 + dfs(amount - c))
            # return dp[i]
            memo[amount] = res
            return res
        # return dfs(12)
        count = dfs(amount)
        return -1 if count == float('inf') else count