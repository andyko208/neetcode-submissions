class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # keep pointers for each
        # extend the rest if one reaches the end
        w1, w2 = 0, 0
        merged = []
        while w1 < len(word1) and w2 < len(word2):
            merged.append(word1[w1])
            merged.append(word2[w2])
            w1 += 1
            w2 += 1
        # finisht the rest
        if w1 == len(word1) and w2 < len(word2):
            merged.extend(word2[w2:])
        elif w2 == len(word2) and w1 < len(word1):
            merged.extend(word1[w1:])
        return "".join(merged)