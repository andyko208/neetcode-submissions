class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # DP to keep the minimum cost to reach the top 
        # dfs function that returns minimum cost 
        # n = len(cost)
        # # cache the cost at each index of -1
        # dp = [-1] * n
        # def dfs(i):
        #     # base case to return 0 if i == n
        #     if i >= n:
        #         return 0
        #     if dp[i] != -1:
        #         return dp[i]
        #     # return the cached amount if not -1
        #     # total = cost[i] + min(dfs(i+1), dfs(i+2))
        #     dp[i] = cost[i] + min(dfs(i+1), dfs(i+2))
        #     return dp[i]
        #     # return total
        # # get the max of dfs(0), dfs(1)
        # return min(dfs(0), dfs(1))

        # # Bottom up
        # # dp[i] represents the minimum cost needed to reach i
        # n = len(cost)
        # # memoize a dp list of size n for 0
        # dp = [0] * (n+1)
        # # iterate from 2 to n+1
        # for i in range(2, n+1):
        #     # set dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        #     dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        # # return dp[n]
        # return dp[n]

        # Space optimized
        n = len(cost)
        # let cost at i represent the minimium cost needed to reach n
        # start from len(cost) - 3 to += by minimum of cost[i+1] and cost[i+2]
        for i in range(n-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])


