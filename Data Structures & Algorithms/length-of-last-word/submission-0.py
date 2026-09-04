class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # split the string in to a list
        splitted = s.strip().split()
        # get the length of the last word
        return len(splitted[-1])