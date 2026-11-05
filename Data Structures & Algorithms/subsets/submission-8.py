class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Time: O(n*2^n) - recursion form take or skip and appending the copy
        # Space: O(n) - recursion depth can grow up to the size of nums
        # define a list to return
        res = []
        # define a recursive function to add subsets to res
        def dfs(i, subset):
            # base case to append the copy of subset to res
            if i == len(nums):
                res.append(subset.copy())
                return
            # append nums at i to subset
            subset.append(nums[i])
            # recurse through
            dfs(i+1, subset)
            # backtrack
            subset.pop()
            # recurse through
            dfs(i+1, subset)
        dfs(0, [])
        return res

# i = 0, subset = []
# i = 1, subset = [1]
# i = 2, subset = [1, 2]
# i = 3, subset = [1, 2, 3] -> res = [[1, 2, 3]]
# i = 3, subset = [1, 2] -> res = [[1, 2, 3], [1, 2]]
# i = 2, subset = [1]
# i = 3, subset = [1, 3] -> res = [[1, 2, 3], [1, 2], [1, 3]]
# i = 3, subset = [1] -> res = [[1, 2, 3], [1, 2], [1, 3], [1]]
# i = 1, subset = []
# i = 2, subset = [2]
# i = 3, subset = [2, 3] -> res = [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3]]
# i = 3, subset = [2] -> res = [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2]]
# i = 2, subset = []
# i = 3, subset = [3] -> res = [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3]]
# i = 3, subset = [] -> res = [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]

