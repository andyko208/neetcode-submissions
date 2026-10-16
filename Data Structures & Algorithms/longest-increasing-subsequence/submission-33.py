class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Bottom Up DP
        n = len(nums)
        # memoize a 1D dp list of 1s of size n+1
        dp = [1] * (n+1)
        # iterate i from n-1 to 0
        for i in range(n-1, -1, -1):
            # iterate j from i+1 to n
            for j in range(i+1, n):
                # find bigger value to its right
                if nums[i] < nums[j]:
                    # maximize LIS to 1 + dp[j]
                    dp[i] = max(dp[i], 1 + dp[j])
        # return max(dp)
        return max(dp)