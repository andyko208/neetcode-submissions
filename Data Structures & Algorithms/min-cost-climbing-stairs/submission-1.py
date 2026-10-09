class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # DP to keep the minimum cost to reach the top 
        # dfs function that returns minimum cost 
        n = len(cost)
        # cache the cost at each index of -1
        dp = [-1] * n
        def dfs(i):
            # base case to return 0 if i == n
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            # return the cached amount if not -1
            # total = cost[i] + min(dfs(i+1), dfs(i+2))
            dp[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return dp[i]
            # return total
        # get the max of dfs(0), dfs(1)
        return min(dfs(0), dfs(1))