class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Bottom Up DP
        n = len(nums)
        # memoize a 1D dp list of 1s of size (n+1)
        dp = [1] * (n+1)
        # iterate i from n-1 to 0
        for i in range(n-1, -1, -1):
            # iterate j from i+1 to n
            for j in range(i+1, n):
                # check if there is an increasing subsequence to its right
                if nums[i] < nums[j]:
                    # update the max increasing subsequence at i
                    dp[i] = max(dp[i], 1 + dp[j])
        # return the max of the increasing subsequence at any index
        return max(dp)