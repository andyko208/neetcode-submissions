class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # define a list to return
        res = []
        # sort nums
        nums.sort()
        # define a recursive function with backtracking
        def dfs(i, subset, total):
            # base case to append subset to res
            if total == target:
                res.append(subset.copy())
                return
            # iterate j from i to n
            for j in range(i, len(nums)):
                # check if valid to append nums at i
                if total + nums[j] > target:
                    return
                # append nums at i
                subset.append(nums[j])
                # recurse
                dfs(j, subset, total + nums[j])
                # backtrack
                subset.pop()
                # # recurse again
                # dfs(j, subset, total)
        dfs(0, [], 0)
        return res