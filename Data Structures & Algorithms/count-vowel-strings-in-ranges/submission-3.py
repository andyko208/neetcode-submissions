class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        validity_sums = [0] * (n+1) # Space: O(N)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        # create a list to store validity of vowel string in words with length of words
        # optimize by keeping track of
        curSum = 0
        for i in range(n): # Time: O(N)
            validity_sums[i+1] = validity_sums[i]
            if words[i][0] in vowels and words[i][-1] in vowels:
                validity_sums[i+1] = validity_sums[i] + 1
        # iterate through queries and sum up slices of validity string within the query range
        # print(validity_sums)
        res = []
        for li, ri in queries: # Time: O(k)
            res.append(validity_sums[ri + 1] - validity_sums[li])
        # append each count to the res list
        return res