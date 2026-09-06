class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # # Brute force approach
        # # create a hashset of vowels
        # vowels = set(['a', 'e', 'i', 'o', 'u'])
        # # create a binary list to tell whether words[i] is valid or not
        # n = len(words)
        # valids = [0] * n
        # # Time: O(N+k), Space: O(n)
        # for i in range(n): # O(N)
        #     if words[i][0] in vowels and words[i][-1] in vowels:
        #         valids[i] = 1
        # print(valids)
        # # iterate through queries and sum up the rangein the binary list 
        # res = []
        # for li, ri in queries:
        #     res.append(sum(valids[li:ri+1])) # O(k)
        # return res

        # Optimized approach
        # use prefix sum so that sum operation can be replaced with a simple look up of O(1)
        
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        # create a prefix sum to tell at index i how many elements are valid
        n = len(words)
        prefixSum = [0] * (n+1)
        # curSum = 0
        # [0, 1, 1, 2, 3, 4]
        for i in range(n):
            prefixSum[i+1] = prefixSum[i]
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefixSum[i+1] += 1
        # print(prefixSum)
        # [0, 1, 2, 3]
        res = []
        # Utilize prefixSum to get the sum total
        for li, ri in queries:
            res.append(prefixSum[ri+1] -  prefixSum[li])

        return res




