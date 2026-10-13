class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # # create a defs function that takes in i
        # n = len(nums)
        # dp = [1] * n
        # for i in range(n-1, -1, -1):
        #     for j in range(i+1, n):
        #         if nums[i] < nums[j]:
        #             dp[i] = max(dp[i], 1 + dp[j])
        # return max(dp)

        n = len(nums)
        dp = [-1] * (n+1)
        dp[n] = 0
        def dfs(i):
            # if i == n:
            #     return 0
            if dp[i] != -1:
                return dp[i]
            res = 1
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    res = max(res, 1 + dfs(j))
            dp[i] = res
            return res
        return max(dfs(i) for i in range(n))