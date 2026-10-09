class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # recurse using 2 indices, i to represent prev and j for cur
        n = len(nums)
        # memoize using 2D list of -1s
        dp = [[-1] * n for _ in range(n)]
        def dfs(i, j):
            # base case to return 0 if j == n
            if j == n:
                return 0
            # return dp[i][j] if not -1
            if dp[i][j] != -1:
                return dp[i][j]
            # res = dfs(i, j+1)
            res = dfs(i, j+1)
            # if i == -1 or nums[i] < nums[j], res = max(res, 1 + dfs(j, j+1)))
            if i == -1 or nums[i] < nums[j]:
                res = max(res, 1 + dfs(j, j+1))
            # return res
            dp[i][j] = res
            return res
        # return dfs(-1, 0)
        return dfs(-1, 0)