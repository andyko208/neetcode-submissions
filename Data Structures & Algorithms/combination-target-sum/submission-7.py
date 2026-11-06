class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Time: O((target / min(nums) * 2^(target / min(nums)))
        # Space: O(target / min(nums))
        # define a list to return
        res = []
        # sort nums
        nums.sort()
        # define a recursive function with backtracking
        def dfs(i, subset, total):
            # base case to append subset to res
            if total == target:
                # O(target / min(nums))
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
        dfs(0, [], 0)
        return res

# nums = [1, 2, 3], target = 3
# dfs(0, [], 0)
# dfs(0, [1], 1)
# dfs(0, [1, 1], 2)
# dfs(0, [1, 1, 1], 3) -> res = [[1, 1, 1]]
# dfs(1, [1, 2], 3) -> res = [[1, 1, 1], [1, 2]]
# dfs(2, [3], 3) -> res = [[1, 1, 1], [1, 2], [3]]