class Solution:
    def maxScore(self, s: str) -> int:
        # Brute force approach
        # # iterate i from 0 to n
        # n = len(s)
        # max_sum = 0
        # for i in range(n-1):
        #     # max_sum = max(max_sum, sum(0:i) + sum(i+n))
        #     l = Counter(s[:i+1])['0']
        #     r = Counter(s[i+1:n])['1']
        #     cur_sum = l + r
        #     max_sum = max(max_sum, cur_sum)
        #     # print(cur_sum, max_sum)
        # return max_sum
        
        # Prefix sum by treating 0 as -1
        # find the smallest value index
        # the right is automatically set
        n = len(s)
        max_count = 0
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            # print(left, right)
            max_count = max(max_count, left.count("0") + right.count("1"))
        return max_count