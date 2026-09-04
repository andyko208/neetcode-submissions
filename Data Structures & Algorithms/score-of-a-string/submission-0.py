class Solution:
    def scoreOfString(self, s: str) -> int:
        # keep a prev pointer that starts at 0
        prev = 0
        curSum = 0
        # iterate from 1 to len(s) to accumulate absolute sum of s[i] - s[prev]
        for i in range(len(s)):
            curSum += abs(ord(s[i]) - ord(s[prev]))
            # set prev to i
            prev = i
        return curSum