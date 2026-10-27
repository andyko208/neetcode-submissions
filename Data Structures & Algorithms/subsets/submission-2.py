class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # create a list to return
        res = []
        # define a recursive function recurses through all variations
        def dfs(i, cur):
            # base case to return
            if i == len(nums):
                res.append(cur.copy())
                return
            
            # recursion of taking the current element 
            cur.append(nums[i])
            dfs(i+1, cur)
            
            # recursion of not taking the current element
            cur.pop()
            dfs(i+1, cur)
        
        dfs(0, [])
        return res