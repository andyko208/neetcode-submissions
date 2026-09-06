class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # Brute force approach
        # create a hashset of vowels
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        # create a binary list to tell whether words[i] is valid or not
        n = len(words)
        valids = [0] * n
        for i in range(n):
            if words[i][0] in vowels and words[i][-1] in vowels:
                valids[i] = 1
        print(valids)
        # iterate through queries and sum up the rangein the binary list 
        res = []
        for li, ri in queries:
            res.append(sum(valids[li:ri+1]))
        return res