class Solution:
    def romanToInt(self, s: str) -> int:
        # create a hashmap of value to symbol 
        symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        # iterate from the back of the string and keep a previous character for 4, 9 cases
        total = 0
        prev = None
        for i in range(len(s)-1, -1, -1):
            if (prev == "V" or prev == "X") and s[i] == "I":
                total -= symbols[s[i]]
            elif (prev == "L" or prev == "C") and s[i] == "X":
                total -= symbols[s[i]]
            elif (prev == "D" or prev == "M") and s[i] == "C":
                total -= symbols[s[i]]
            else:
                total += symbols[s[i]]
                prev = s[i]
        # if prev is X and next is I, subtract by I rather than add
        return total