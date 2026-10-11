class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # # Basic recursion
        # # recurse through to get the minimum b/ i+1 and i+2
        # def dfs(i):
        #     # base case to return 0 if reached the end
        #     if i >= len(cost):
        #         return 0
        #     # current cost + smaller cost from taking i+1 or i+2
        #     return cost[i] + min(dfs(i+1), dfs(i+2))
        # # return the smaller cost b/ starting at 0 vs 1
        # return min(dfs(0), dfs(1))
    
        # Top Down DP
        n = len(cost)
        # cache a 1D dp list of -1s 
        dp = [-1] * n
        def dfs(i):
            # base case to return 0 if reached the end
            if i >= n:
                return 0
            # utilize cache to save work
            if dp[i] != -1:
                return dp[i]
            # update dp list for total cost at ith floor
            dp[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return dp[i]
        # return the smaller cost b/ starting at 0 vs 1
        return min(dfs(0), dfs(1))
        