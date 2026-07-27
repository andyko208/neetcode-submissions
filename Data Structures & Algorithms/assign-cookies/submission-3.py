class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Objective: maximize # of content children = how can we maximize distribution of
        #               limited # of cookies to each of children with lowest g?

        # Return: max number of content children
        # two pointers, l and r to compare each other
        # loop until l < len(g) or r < len(s), increment counter is g[l] == s[r]
        l, r, counter = 0, 0, 0
        g.sort()
        s.sort()
        while l < len(g) and r < len(s):
            if g[l] <= s[r]:
                counter, l = counter + 1, l + 1
            r += 1
        return counter
# [1, 2, 2, 3, 10]
# [1, 2, 3, 4]