class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Recursive - Time: O(n * 2^n), Space: O(n)
        # # create a list to return
        # res = []
        # # define a recursive function recurses through all variations
        # def dfs(i, cur):
        #     # base case to return
        #     if i == len(nums):
        #         # takes up O(N)
        #         res.append(cur.copy())
        #         return
            
        #     # recursion of taking the current element 
        #     cur.append(nums[i])
        #     dfs(i+1, cur)
            
        #     # recursion of not taking the current element
        #     cur.pop()
        #     dfs(i+1, cur)
        
        # dfs(0, [])
        # return res

        # iterative - Time: O(n*2^n), Space: O(n)
        # define a list to return
        res = [[]]
        # iterate through num in nums
        # for each element in res, add num to it
        for num in nums:
            res += [r + [num] for r in res]
        return res



