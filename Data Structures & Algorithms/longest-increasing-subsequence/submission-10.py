class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # recurse on the next index
        n = len(nums)
        # cache 1D dp list of -1s
        dp = [-1] * (n+1)
        # define recursive function dfs that takes in i and j
        def dfs(i, j):
            # base case to return 0 if j == n
            if j == n:
                return 0
            # return early using memoization
            if dp[i] != -1:
                return dp[i]
            # res = dfs(i, j+1)
            res = dfs(i, j+1)
            # if nums[i] == -1 or nums[i] < nums[j], res = max(res, 1 + dfs(j, j+1))
            if i == -1 or nums[i] < nums[j]:
                res = max(res, 1 + dfs(j, j+1))
            # return max
            dp[i] = res
            return dp[i]
        return dfs(-1, 0)