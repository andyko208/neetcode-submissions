class Solution:
    def countSubstrings(self, s: str) -> int:
        # two pointer: iterate i from 0 to n and try to expand left and right for additional string if s[l] == s[r]
        n = len(s)
        count = 0
        for i in range(n):
            l, r = i, i
            # odd len palindromic string
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l, r = l - 1, r + 1
            # even len palindromic string
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l, r = l - 1, r + 1
        return count