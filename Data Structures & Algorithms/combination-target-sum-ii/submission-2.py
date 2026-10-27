class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # define a list to return
        res = []
        # sort candidates in increasing order
        candidates.sort()

        # define a recursive function to find combinations
        def dfs(i, subset, total):
            # base case to append subset to res
            if total == target:
                res.append(subset.copy())
                return
            # termination condition
            if i == len(candidates):
                return 
            
            # check whether it's valid to append current element in candidates to subset
            if total + candidates[i] > target:
                return
            
            # append candidates[i] to subset
            subset.append(candidates[i])
            # recurse to find combinations
            dfs(i+1, subset, total + candidates[i])
            # backtracking to try the next possible combination
            subset.pop()
            # shift i to remove adding duplicate elements to res
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, subset, total)
        
        dfs(0, [], 0)
        return res

        # candidates = [1, 2, 2], target = 3

        # dfs(1, [1], 1) -> dfs(2, [1, 2], 3)
        # dfs(3, [], 0)

        # subset = [] 
        # res = [[1, 2]]

    