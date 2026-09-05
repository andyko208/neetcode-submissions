class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        words_validity = [0] * n # Space: O(N)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        # create a list to store validity of vowel string in words with length of words
        for i in range(n): # Time: O(N)
            if words[i][0] in vowels and words[i][-1] in vowels:
                words_validity[i] = 1
        # iterate through queries and sum up slices of validity string within the query range
        res = []
        for li, ri in queries: # Time: O(k)
            res.append(sum(words_validity[li:ri+1])) # O(k)
        # append each count to the res list
        return res