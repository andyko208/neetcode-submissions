class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # maintain a hashamp until a duplicate is found
        mapp = {}
        n = len(s)
        l = -1
        length = 0
        for i in range(n):
            if s[i] in mapp:
                tmp = mapp[s[i]]
                # if duplicate is found, all the elements that come before it must be removed
                for j in range(mapp[s[i]], l, -1):
                    mapp.pop(s[j])
                # update the length after removing
                l = tmp
            mapp[s[i]] = i
            length = max(length, len(mapp))
        return length
        
