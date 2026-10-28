class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # list to return
        res = []

        # # sort nums
        # nums.sort()

        # define recursive function to find all combination sum
        def dfs(i, subset, total):
            # base case check if total == target to add to res
            if total == target:
                res.append(subset.copy())
                return
            # base case to return if i == len(nums)
            if i == len(nums):
                return

            # iterate j from i to len(nums)
            for j in range(i, len(nums)):
                # perform a check to whether it's valid to append nums[i] to subset
                if total > target:
                    return
                # append nums[i] to subset
                subset.append(nums[j])
                # recurse through
                dfs(j, subset, total + nums[j])
                # backtrack
                subset.pop()
            
        dfs(0, [], 0)
        return res