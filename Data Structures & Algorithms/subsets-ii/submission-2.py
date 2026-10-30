class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Time: O(n * 2^n), Space: O(n)
        # define a list to return
        res = []

        # sort nums
        nums.sort()

        # define a recursive function to find and append all combinations with no dup
        def dfs(i, subset):
            # base case to append the copy of subset to res
            if i == len(nums):
                res.append(subset.copy())
                return
            
            # append nums[i] to subset
            subset.append(nums[i])
            # recurse
            dfs(i+1, subset)
            # backtrack
            subset.pop()
            # avoid dup by skipping index where nums[i] == nums[i+1]
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, subset)
        
        dfs(0, [])
        return res
# nums = [1]
# subset = [1]
# res = [[1], []]
