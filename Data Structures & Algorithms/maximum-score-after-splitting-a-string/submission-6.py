class Solution:
    def maxScore(self, s: str) -> int:
        # count up the ones
        ones = s.count("1")
        zeros = 0
        max_score = 0
        # iterate through s and subtract by 1 if s[i] == 1, increment zeros by 1 if s[i] == 0
        for i in range(len(s)-1):
            if s[i] == "1":
                ones -= 1
            elif s[i] == "0":
                zeros += 1
            # update the max = max(max, zeros + ones)
            max_score = max(max_score, ones + zeros)
        return max_score
