class Solution:
    def rob(self, nums: List[int]) -> int:
        # maintain a dp list
        dp = [-1] * len(nums)
        # define a recursive function with i as arg
        def dfs(i):
            # base case to return 0 if i >= len(nums)
            if i >= len(nums):
                return 0
            # save work by returningn early
            if dp[i] != -1:
                return dp[i]
            # set dp[i] to max num[i], two steps ahead with one step ahead
            dp[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            return dp[i]
        # run the recursive function initially with 0
        return dfs(0)