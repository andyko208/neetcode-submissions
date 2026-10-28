class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # define a list to return
        res = []

        # sort nums
        nums.sort()

        # define a recursive function
        def dfs(i, subset):
            # base case to append subset to res
            if i == len(nums):
                res.append(subset.copy())
                return
            
            # append nums[i] to subset
            subset.append(nums[i])
            # take the current element
            dfs(i+1, subset)
            # backtrack
            subset.pop()
            # avoid duplicate
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            # skip the current element and avoid duplicate
            dfs(i+1, subset)
            
        dfs(0, [])
        return res

# [1, 2, 2]
# dfs(0, []) -> dfs(1, [1]) -> dfs(2, [1, 2]) -> dfs(3, [1, 2, 2])
#                              dfs(2, [1, 2]) -> dfs(3, [1, 2])
#               dfs(1, []) -> dfs(2, [2]) -> dfs(3, [2, 2])
#                             dfs(2, [2]) -> dfs(3, [2])
#               dfs(3, [])

# res = [[1, 2, 2], [1, 2], [1], [2, 2], [2], []]