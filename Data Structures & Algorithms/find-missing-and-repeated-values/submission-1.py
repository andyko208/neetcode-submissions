class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        nums = [i+1 for i in range(len(grid)**2)]
        vals = {}
        res = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if grid[i][j] in vals:
                    vals[grid[i][j]] += 1
                else:
                    vals[grid[i][j]] = 1
        # print(vals)
        for key, val in vals.items():
            # print(key, val)
            if val == 2:
                res.append(key)
                break
        repeat = [num for num in nums if num not in list(vals.keys())]
        res += repeat
        return res