class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # create a hashset of words
        words_set = set(words)
        res = set()
        # iterate through the words hashset and check if current word is in the each word of hashset
        # Time: O(k^2), Space: O(k)
        for w in words_set:
            for word in words_set:
                if w != word and w in word:
                    res.add(w)
        return list(res)

            