class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # keep a total
        total = sum(nums)
        n = len(nums)
        # no way to split odd number into half
        if total % 2 == 1:
            return False
        # recurse through using a for loop to try all possible ones
        def dfs(i, remaining):
            if i >= n:
                return True if remaining == 0 else False
            if remaining == 0:
                return True
            # take or skip
            return dfs(i+1, remaining - nums[i]) or dfs(i+1, remaining)
        return dfs(0, sum(nums) // 2)
            