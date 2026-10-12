class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # start from n-1 to 0
        n = len(nums)
        # memoize 1D dp list to save compute
        dp = [-1] * (n+1)
        # recurse by running dfs(i-1)
        def dfs(i):
            if dp[i] != -1:
                return dp[i]
            best = 1
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    best = max(best, 1 + dfs(j))
                dp[i] = best
            return best
        return max(dfs(i) for i in range(n))