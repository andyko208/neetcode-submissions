class Solution:
    def rob(self, nums: List[int]) -> int:
        # compare whether taking the second is better than the first to add to the current amount
        
        # define a recursive function that takes in value at nums[0]
        n = len(nums)
        dp = [-1] * (n+1)
        def dfs(i):
            # base case to return 0 if i >= n
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            # res = dfs(i+2)
            dp[i] = max(dfs(i+1), nums[i] + dfs(i+2))
            return dp[i]
            # return res
        # return max(dfs(0), dfs(-1))
        return dfs(0)
