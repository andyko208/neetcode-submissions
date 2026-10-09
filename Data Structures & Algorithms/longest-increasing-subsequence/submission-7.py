class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # # recurse using 2 indices, i to represent prev and j for cur
        # n = len(nums)
        # # memoize using 2D list of -1s
        # dp = [[-1] * n for _ in range(n)]
        # def dfs(i, j):
        #     # base case to return 0 if j == n
        #     if j == n:
        #         return 0
        #     # return dp[i][j] if not -1
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     # res = dfs(i, j+1)
        #     res = dfs(i, j+1)
        #     # if i == -1 or nums[i] < nums[j], res = max(res, 1 + dfs(j, j+1)))
        #     if i == -1 or nums[i] < nums[j]:
        #         res = max(res, 1 + dfs(j, j+1))
        #     # return res
        #     dp[i][j] = res
        #     return res
        # # return dfs(-1, 0)
        # return dfs(-1, 0)

        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(i - 1, -2, -1):
                LIS = dp[i + 1][j + 1]  # Not including nums[i]
                if j == -1 or nums[j] < nums[i]:
                    LIS = max(LIS, 1 + dp[i + 1][i + 1])  # Including nums[i]
                dp[i][j + 1] = LIS
        return dp[0][0]


