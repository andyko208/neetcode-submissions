class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # maintain a hashamp until a duplicate is found
        mapp = set()
        n = len(s)
        l = 0
        res = 0
        for r in range(n):
            while s[r] in mapp:
                mapp.remove(s[l])
                l += 1
            mapp.add(s[r])
            res = max(res, r - l + 1)
        return res
        
