class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # one ptr 0 and the other len(s)-1
        # another ptr temp to replace one after another
        # run it while one ptr < len(s)-1
        # odd len string will not need to swap the center element
        l = 0
        r = len(s)-1
        temp = None
        while l < r:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l += 1
            r -= 1
        return s
        