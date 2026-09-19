class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # keep defaultdict of -1
        charMap = defaultdict(lambda: -1)
        # keep l
        l = 0
        # keep max_len
        max_len = 0
        # iterate r from 0 to n
        for r in range(len(s)):
            # duplicate char exists in the window
            if charMap[s[r]] > -1:
                # adjust window up to previous duplicate element's index
                while l <= charMap[s[r]]:
                    # hashmap[s[l]] = -1
                    charMap[s[l]] = -1
                    # l += 1
                    l += 1
            # hashmap[s[r]] = r
            charMap[s[r]] = r
            # max_len = max(max_len, r - l + 1)
            max_len = max(max_len, r - l + 1)
        # return max_len
        return max_len
