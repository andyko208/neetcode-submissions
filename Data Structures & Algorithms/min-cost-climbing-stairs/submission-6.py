class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # # Basic recursion
        # # recurse through to get the minimum b/ i+1 and i+2
        # def dfs(i):
        #     # base case to return 0 if i == n
        #     if i >= len(cost):
        #         return 0
        #     # current cost + smaller cost from taking i+1 or i+2
        #     return cost[i] + min(dfs(i+1), dfs(i+2))
        # # smaller cost from starting 0 or 1
        # return min(dfs(0), dfs(1))
    
        # Top Down DP
        n = len(cost)
        dp = [-1] * (n+1)
        def dfs(i):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return dp[i]
        return min(dfs(0), dfs(1))
        