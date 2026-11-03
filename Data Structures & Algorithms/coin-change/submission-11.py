class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # define a recursive function that takes in amount
        dp = [0] * (amount + 1)
        def dfs(total):
            # base case to return 0 if amount == 0
            if total <= 0:
                return 0 if total == 0 else float('inf')
            # memoization
            # print(total)
            if dp[total] != 0:
                return dp[total]
            res = float('inf')
            # iterate through c in coins
            for c in coins:
                # res = min(res, 1 + dfs(amount-c))
                res = min(res, 1 + dfs(total - c))
            # update dp at amount to res
            dp[total] = res
            # return dp at amount
            return dp[total]
        minCoins = dfs(amount)
        return minCoins if minCoins != float('inf') else -1