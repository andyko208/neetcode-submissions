class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # keep two pointers w1 and w2
        w1, w2 = 0, 0
        merged = []
        # while the length of merged char < len(word1) + len(word2)
        while len(merged) < len(word1) + len(word2):
            # if w1 < len(word1), append w1 to merged and w1+=1
            if w1 < len(word1):
                merged.append(word1[w1])
                w1 += 1
            # if w2 < len(word2), append w2 to merged and w2+=1
            if w2 < len(word2):
                merged.append(word2[w2])
                w2 += 1
        # join the list as a string and return it
        return "".join(merged)