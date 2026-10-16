class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # keep a max left and max right

        maxLeft, maxRight = [0] * n, [0] * n
        maxLeft[0] = height[0]
        maxRight[n-1] = height[n-1]
        # get their min
        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i-1], height[i])
        for i in range(n-2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i])
        
        total = 0
        # iterate i from 0 to n
        for i in range(n):
            total += min(maxLeft[i], maxRight[i]) - height[i]
        # accumulate the sum of min(min(l, r) - height[i], 0)
        return total