class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # create a hashset of words
        res = set()
        # iterate through the words hashset and check if current word is in the each word of hashset
        # Time: O(N^2), Space: O(N)
        for w1 in words:
            for w2 in words:
                if w1 != w2 and w1 in w2:
                    res.add(w1)
                    break
        return list(res)

            