class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        # need a res list to return
        res = []
        # sort nums in increasing order
        candidates.sort()

        # define a recursive function that recurses through the find the combinations        
        def dfs(i, cur, total):
            # base case to append cur to res
            if total == target:
                res.append(cur.copy())
                return
            if i == len(candidates):
                return
            
            # check if adding current element is valid
            if total + candidates[i] > target:
                return 
            # otherwise, append to cur
            cur.append(candidates[i])
            # recurse on i+1
            dfs(i+1, cur, total + candidates[i])
            # backtrack
            cur.pop()

            # skip the duplicate elements
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, cur, total)
        
        dfs(0, [], 0)
        return res

# Time: O(2^n * n), Space: O(n)
# [1, 2, 3], target = 3

# base case to append the copy of cur list to res
# total + 1 > target, return

# dfs(0, [], 0) -> dfs(1, [1], 1) -> dfs(2, [1, 2], 3)

# res = [[1, 2], [3]]

