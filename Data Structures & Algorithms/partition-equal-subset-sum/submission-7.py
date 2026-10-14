class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        # return false if sum(nums) % 2 == 1:
        if total % 2 == 1:
            return False
        # memoize a hashmap of (i, target) to return True if target ever reaches 0
        dp = {}
        for i in range(n+1):
            dp[(i, 0)] = 1
        # define a recursive function that takes in i and remaining
        def dfs(i, target):
            # base case to return True if remaining == 0
            # if target == 0:
            #     return True
            # base case to return False if i == n and target != 0
            # if i >= n:
            #     return True if target == 0 else False
            if i >= n:
                if target == 0:
                    dp[(i, target)] = 1
                    return 1
                else:
                    dp[(i, target)] = 0
                    return 0
            if (i, target) in dp:
                return dp[(i, target)]
            # return dfs(i+1, remaining) or dfs(i+1, remaining = nums[i])
            dp[(i, target)] = dfs(i+1, target) or dfs(i+1, target - nums[i])
            return dp[(i, target)]
        # return dfs(0, sum(nums) // 2)
        return bool(dfs(0, total // 2))