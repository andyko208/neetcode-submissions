class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # check for each character whether we can formulate max length using it
        # as we iterate through, check if the size of the window -  the count of it is less than k
        # if not ok, increment the left pointer by 1 and remove the leftmost window
        charSet = set(s)
        res = 0
        # iterate through the whole unique character to find all possibilities
        for c in charSet:
            count = 0
            l = 0
            for r in range(len(s)):
                # count can be incremented without having to check whether the current element is not equal to the character
                if s[r] == c:
                    count += 1
                while r - l + 1 - count > k:
                    # adjust window by removing element from l
                    if c == s[l]:
                        count -= 1
                    l += 1
                res = max(res, r - l + 1)
        return res
                