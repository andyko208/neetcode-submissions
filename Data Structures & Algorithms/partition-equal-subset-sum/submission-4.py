class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        n = len(nums)
        def dfs(i, target):
            if i == n:
                return True if target == 0 else False
            if target < 0:
                return False
            return dfs(i+1, target - nums[i]) or dfs(i+1, target)
        return dfs(0, total // 2)