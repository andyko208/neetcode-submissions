class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # memoize 1D dp list of 0s of size n+1
        dp = [0] * (n+1)
        dp[n] = 0
        # define dfs that takes in i
        def dfs(i):
            # # base case to retun 0 if i == n
            # if i == n:
            #     return 0
            # memoization
            if dp[i] != 0:
                return dp[i]
            # by default LIS is 1
            LIS = 1
            # iterate j from i+1 to n
            for j in range(i+1, n):
                # recurse on j to maximize LIS if nums[i] < nums[j]
                if nums[i] < nums[j]:
                    LIS = max(LIS, 1 + dfs(j))
                # update memoized list
                dp[i] = LIS
            # return LIS
            return LIS
        # return index where LIS is the largest
        return max(dfs(i) for i in range(n))