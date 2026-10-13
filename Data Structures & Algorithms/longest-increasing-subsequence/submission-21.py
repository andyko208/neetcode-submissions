class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # create a defs function that takes in i
        n = len(nums)
        dp = [-1] * (n+1)
        def dfs(i):
            # base case to return 0 if i == n
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            # iterate j from i+1 to n
            res = 1
            for j in range(i+1, n):
                # if nums[i] < nums[j], res += 1 + dfs(j)
                if nums[i] < nums[j]:
                    res = max(res, 1 + dfs(j))
            dp[i] = res
            return res
        # return max([dfs(n) for n in nums])
        return max(dfs(i) for i in range(n))