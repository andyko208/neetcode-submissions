class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # find two things and return as lilst: [repeating element, missing element]
        seen = set()
        res = []
        for r in grid:
            for c in r:
                # found repeat
                if c in seen:
                    res.append(c)
                else:
                    seen.add(c)
        for i in range(1, len(grid)**2+1):
            if i not in seen:
                res.append(i)
        return res