class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_map, s_map = {}, {}
        n = len(pattern)
        s_split = s.split() # turn s into match indices of pattern string

        # cannot perform bijection if lengths differ
        if len(pattern) != len(s_split):
            return False

        # iterate i through n len(pattern[i]) == len(s.split(' ')[i])
        for i in range(n):
            # check the bijection works
            if pattern[i] in p_map and p_map[pattern[i]] != s_split[i]:
                return False
            if s_split[i] in s_map and s_map[s_split[i]] != pattern[i]:
                return False
            # map char from pattern to word in s
            p_map[pattern[i]] = s_split[i]
            # the other way around
            s_map[s_split[i]] = pattern[i]
        return True