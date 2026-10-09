class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # recursive call to use all
        # dp list to len amount + 1 of val amount
        memo = {}
        memo[0] = 0
        # define dfs that takes in amount
        for a in range(1, amount+1):
            res = float('inf')
            for c in coins:
                if a - c >= 0:
                    res = min(res, 1 + memo[a - c])
            memo[a] = res
        return memo[amount] if memo[amount] != float('inf') else -1
        