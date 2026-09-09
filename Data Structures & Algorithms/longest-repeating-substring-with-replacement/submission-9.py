class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # keep a hashmap of chars
        char_window = defaultdict(int)
        # keep a pointer l
        l = 0
        max_len = 0
        # keep track of the max character and its count
        max_count = 0
        n = len(s)
        # iterate r from 0 to n
        for r in range(n):
            # whenever a non max character appears, check whether the difference between the current window size and the count of non max characters
            # add a new char to the window
            char_window[s[r]] += 1
            # update max_char and max_count
            if char_window[s[r]] > max_count:
                max_count = char_window[s[r]]
            # remove element from the left until substring is valid again
            while (r - l + 1) - max_count > k:
                char_window[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len
