class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # define variables
        n = len(candidates)
        subsets = []
        # sort candidates
        candidates.sort()
        # define a recursive that appends a copy of subset to subsets
        def dfs(i, subset, total):
            # base case 1: append subset.copy to subsets
            if total == target:
                subsets.append(subset.copy())
                return
            # base case 2: return when i is out of bounds
            if i == len(candidates):
                return 
            
            # check if valid to append nums at i to subset
            if total + candidates[i] > target:
                return
            # append candidates at i to subset
            subset.append(candidates[i])
            # recurse through
            dfs(i+1, subset, total + candidates[i])
            # backtrack
            subset.pop()
            # skip over duplicate elements
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            # recurse
            dfs(i+1, subset, total)
        
        dfs(0, [], 0)
        return subsets
# [1, 2, 2, 4, 5, 6, 9]
# [1, 2, ]
