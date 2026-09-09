class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # create a set to hold a window of chars
        char_window = set()
        # keep a pointer l
        l = 0
        max_len = 0
        # iterate r from 0 to n
        for r in range(len(s)):
            # while s[r] is in the set, to remove from s[l] from the set and l += 1
            while s[r] in char_window:
                char_window.remove(s[l])
                l += 1
            # update the max len to be r - l + 1
            max_len = max(max_len, r - l + 1)
            # add s[r] in the set
            char_window.add(s[r])
        return max_len