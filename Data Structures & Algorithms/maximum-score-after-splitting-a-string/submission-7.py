class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        # create a prefix sum from left to right for 0s
        prefixSum = [0] * n
        # create a suffix sum from right to left for 1s
        suffixSum = [0] * n
        curSum = 0
        for i in range(n-1): # should have at least one element on right
            if s[i] == '0':
                curSum += 1
            prefixSum[i] = curSum
        print(prefixSum)
        
        curSum = 0
        for i in range(n-1, 0, -1):
            if s[i] == '1':
                curSum += 1
            suffixSum[i] = curSum
        print(suffixSum)
        
        # iterate through to find the max sum of each
        maxSum = 0
        for i in range(n-1):
            maxSum = max(maxSum, prefixSum[i] + suffixSum[i+1])

        return maxSum
