class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # return False if sum(nums) % 2 == 1
        total = sum(nums)
        n = len(nums)
        if total % 2 == 1:
            return False
        # define dfs that takes in i and remaining
        def dfs(i, remaining):
            # base case to return True if remaining == 0
            if remaining == 0:
                return True
            # return False if i >= n and target != 0
            if i >= n and remaining != 0:
                return False
            # return recurse on i+1 with remaining - nums[i] or recurse on i+1 with remaining
            return dfs(i+1, remaining - nums[i]) or dfs(i+1, remaining)
        # return dfs(0, sum(nums) // 2)
        return dfs(0, total // 2)