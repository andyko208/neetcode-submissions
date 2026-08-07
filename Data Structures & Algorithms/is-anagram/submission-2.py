class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash, t_hash = {}, {}
        for c in s:
            if c in s_hash:
                s_hash[c] += 1
            else:
                s_hash[c] = 1
        for c in t:
            if c in t_hash:
                t_hash[c] += 1
            else:
                t_hash[c] = 1
        print(s_hash, t_hash)
    
        return s_hash == t_hash