class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # # recurse on the next index
        # n = len(nums)
        # # cache 1D dp list of -1s
        # dp = [-1] * (n+1)
        # # define recursive function dfs that takes in i and j
        # def dfs(i, j):
        #     # base case to return 0 if j == n
        #     if j == n:
        #         return 0
        #     # return early using memoization
        #     if dp[i] != -1:
        #         return dp[i]
        #     # res = dfs(i, j+1)
        #     res = dfs(i, j+1)
        #     # if nums[i] == -1 or nums[i] < nums[j], res = max(res, 1 + dfs(j, j+1))
        #     if i == -1 or nums[i] < nums[j]:
        #         res = max(res, 1 + dfs(j, j+1))
        #     # return max
        #     dp[i] = res
        #     return dp[i]
        # return dfs(-1, 0)

        # Bottom up DP
        # n = len(nums)
        # dp = [[0] * (n+1) for _ in range(n+1)]
        # for i in range(n-1, -1, -1):
        #     for j in range(i-1, -2, -1):
        #         res = dp[i+1][j+1]
        #         if j == -1 or nums[j] < nums[i]:
        #             res = max(res, 1 + dp[i+1][i+1])
        #         dp[i][j+1] = res
        # return dp[0][0]
        
        n = len(nums)
        dp = [1] * n
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)






