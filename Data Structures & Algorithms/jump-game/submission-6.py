class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # define a recursive function to recurse through for all possible pos from nums[i]
        # Time: O(2^n)
        # Space: O(n)
        # base case to return True if i == len(nums)-1
        # memoize by keeping a dp list of 
        memo = {}
        def dfs(i):
            if i >= len(nums)-1:
                return True
            if i in memo:
                return memo[i]
            for j in range(nums[i], 0, -1):
                if dfs(i+j):
                    memo[i] = True
                    return memo[i]
            memo[i] = False
            return memo[i]
        return dfs(0)