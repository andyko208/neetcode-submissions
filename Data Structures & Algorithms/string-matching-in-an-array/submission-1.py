class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # brute force approach
        n = len(words)
        res = set()
        # iterate i from 0 to n
        for i in range(n):
            # iterate j from i + 1 to n
            for j in range(i+1, n):
                # check if words[i] is in words[j]
                if words[i] in words[j]:
                    res.add(words[i])
                elif words[j] in words[i]:
                    res.add(words[j])
        return list(res)