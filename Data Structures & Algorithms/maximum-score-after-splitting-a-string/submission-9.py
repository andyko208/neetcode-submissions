class Solution:
    def maxScore(self, s: str) -> int:
        # n = len(s)
        # # Time: O(N), Space: O(N)
        # # create a prefix sum from left to right for 0s
        # prefixSum = [0] * n
        # # create a suffix sum from right to left for 1s
        # suffixSum = [0] * n
        # curSum = 0
        # for i in range(n-1): # should have at least one element on right
        #     if s[i] == '0':
        #         curSum += 1
        #     prefixSum[i] = curSum
        # # print(prefixSum)
        
        # curSum = 0
        # for i in range(n-1, 0, -1):
        #     if s[i] == '1':
        #         curSum += 1
        #     suffixSum[i] = curSum
        # # print(suffixSum)

        # # iterate through to find the max sum of each
        # maxSum = 0
        # for i in range(n-1):
        #     maxSum = max(maxSum, prefixSum[i] + suffixSum[i+1])

        # return maxSum

        # Time: O(N), Space: O(1)
        # get all ones with .count()
        # iterate through s and decrement ones if '1' is seen and increment zeros if '0' is seen
        ones = s.count('1')
        zeros = 0
        maxSum = 0
        for i in range(len(s)-1): # ensure that there is at least an element on the right
            if s[i] == '1':
                ones -= 1
            elif s[i] == '0':
                zeros += 1
            maxSum = max(maxSum, ones + zeros)
        return maxSum





