class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # create a hashmap to map char of s to char of t
        s_map, t_map = {}, {}
        n = len(s)
        # iterate through and set hashmap[s[i]] = t[i]
        for i in range(n):
            # if a mapping fails in the earlier chars, return immediately
            if (s[i] in s_map and s_map[s[i]] != t[i]) or (t[i] in t_map and t_map[t[i]] != s[i]):
                return False
            s_map[s[i]] = t[i]
            t_map[t[i]] = s[i]

        return True
        
        
