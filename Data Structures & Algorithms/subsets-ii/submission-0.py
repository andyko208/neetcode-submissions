class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # sort nums
        nums.sort()
        # define a list to return
        res = []
        # define a recursive function to find all subsets
        def dfs(i, cur):
            # base case to append copy of current list to res
            if i == len(nums):
                res.append(cur.copy())
                return
            
            # append nums at i to cur
            cur.append(nums[i])
            # recurse on dfs
            dfs(i+1, cur)
            # backtrack
            cur.pop()

            # move i to avoid seeing a dup
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, cur)
        
        dfs(0, [])
        return res

        # [7, 7]
        # dfs(1, [7]) -> dfs(2, [7, 7]) -> dfs(2, [7])
        #             -> dfs(2, [])
        # res = [[7, 7], [7], []]