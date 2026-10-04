class Solution:
    def climbStairs(self, n: int) -> int:
        # Intuition: how many ways 1 and 2 can reach n?
        # recursive
        # def dfs(i):
        #     # base case if i >= n
        #     if i >= n:
        #         return 1 if i == n else 0
        #     # recurse on i+1 and i+2 
        #     return dfs(i+1) + dfs(i+2)
        # # start i at 0
        # return dfs(0)

        # Top down DP
        # cache dp list of len n
        # dp = [-1] * n
        # def dfs(i):
        #     # update dp[i] to be dfs(i+1) and dfs(i+2)
        #     if i >= n:
        #         return 1 if i == n else 0
        #     if dp[i] != -1:
        #         return dp[i]
        #     dp[i] = dfs(i+1) + dfs(i+2)
        #     return dp[i]
        # return dfs(0)

        # Bottom up DP
        # cache dp list by initializing first two to 1 and 2
        # if n <= 1:
        #     return 1
        # dp = [-1] * n
        # dp[0], dp[1] = 1, 2
        # for i in range(2, n):
        #     dp[i] = dp[i-1] + dp[i-2]
        #     print(dp)
        # return dp[-1]

        # Bottom up DP (Space Optimized)
        if n <= 1:
            return 1
        one, two = 1, 2
        for i in range(2, n):
            one, two = one + two, max(one, two)
        return max(one, two)


