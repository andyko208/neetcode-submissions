class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Time: O(n * 2^n), Space: O(n)
        # define a list to return
        res = []
        # define a recursive function to find and append all subsets to res
        def dfs(i, subset):
            # base case to append subset to res
            if i == len(nums):
                # copy the exact element not the memory itself
                res.append(subset.copy())
                return
            
            # append nums at i
            subset.append(nums[i])
            # recurse
            dfs(i+1, subset)
            # backtrack
            subset.pop()
            # recurse
            dfs(i+1, subset)
        
        dfs(0, [])
        return res
