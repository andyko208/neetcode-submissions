class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # find two things and return as lilst: [repeating element, missing element]
        # seen = set()
        # res = []
        # for r in grid:
        #     for c in r:
        #         # found repeat
        #         if c in seen:
        #             res.append(c)
        #         else:
        #             seen.add(c)
        # for i in range(1, len(grid)**2+1):
        #     if i not in seen:
        #         res.append(i)
        # return res
        n = len(grid)
        res = [0] * n **2 
        for r in grid:
            for c in r:
                res[c-1] += 1
        repeat = -1
        dup = -1
        for i in range(len(res)):
            if res[i] == 2:
                repeat = i+1
            if res[i] == 0:
                dup = i+1
            if repeat > 0 and dup > 0:
                break    
        return [repeat, dup]