class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # maintain a hashset of non repeating characters
        charS = set()
        # keep a pointer L to remove from left to until s[L] == s[R]
        L, n = 0, len(s)
        res = 0
        # iterate for loop until n and add new element if not in it
        for R in range(n):
            while s[R] in charS:
                charS.remove(s[L])
                L += 1
            charS.add(s[R])
            # set the length to the maximum of R - L + 1
            res = max(res, R - L + 1)
        return res