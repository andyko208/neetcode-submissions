class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # need a hashmap to track {remaining amount: # of coins needed to reach 0}
        memo = {}
        # define a recursive function that takes in current amount
        def dfs(cur):
            # base case
            if cur == 0:
                return 0
            if cur in memo:
                return memo[cur]
            res = float('inf')
            # iteraete through for loop to try all coins and assign memo[amount] to be the min of all
            for c in coins:
                if cur - c >= 0:
                    res = min(res, 1 + dfs(cur-c))
            memo[cur] = res
            return memo[cur]
        # return res
        # return minAmount if it's greater than the initial value of res set
        minAmount = dfs(amount)
        return -1 if minAmount == float('inf') else minAmount