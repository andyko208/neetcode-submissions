class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time: O(n)
        # Space: O(n)
        # add to the right
        # remove all elements on the left until remove
        l = 0
        seen = set()
        maxLen = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            maxLen = max(maxLen, r - l + 1)
        return maxLen
